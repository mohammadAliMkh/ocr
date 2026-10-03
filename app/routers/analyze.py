from pathlib import Path
from fastapi import APIRouter, File, HTTPException, UploadFile

from app.config import get_settings
from app.services.media import MediaError, detect_kind
from app.schemas import JobSnapshot

from app.services.jobs import JobStore

router = APIRouter(tags=["analyze"])

jobs = JobStore()


@router.post("/analyze", response_model=JobSnapshot)
async def create_analysis(file: UploadFile = File(...)):
    filename = file.filename or "upload"
    try:
        kind = detect_kind(Path(filename), file.content_type)
    except MediaError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    job = jobs.create(kind=kind, filename=filename)
    target = get_settings().upload_dir / f"{job.id}{Path(filename).suffix.lower()}"

    limit = get_settings().max_upload_mb * 1024 * 1024
    written = 0

    try:
        with target.open("wb") as handle:
            while True:
                chunk = await file.read(1024 * 1024)
                if not chunk:

                    break
                written += len(chunk)
                if written > limit:
                    raise HTTPException(status_code=413, detail="File is too large")
                handle.write(chunk)

    except HTTPException:
        target.unlink(missing_ok=True)
        jobs.delete(job.id)
        raise

    job.message = f"File received ({written} bytes)"
    return job.snapshot()
