from pathlib import Path
from uuid import uuid4

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.config import get_settings
from app.services.media import MediaError, detect_kind

router = APIRouter(tags=["analyze"])


@router.post("/analyze")
async def create_analysis(file: UploadFile = File(...)):
    filename = file.filename or "upload"
    try:
        kind = detect_kind(Path(filename), file.content_type)
    except MediaError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    job_id = f"job_{uuid4().hex[:12]}"
    target = get_settings().upload_dir / f"{job_id}{Path(filename).suffix.lower()}"

    written = 0
    with target.open("wb") as handle:
        while True:
            chunk = await file.read(1024 * 1024)
            if not chunk:
                break
            written += len(chunk)
            handle.write(chunk)

    return {"job_id": job_id, "kind": kind, "path": str(target), "size":written}