from pathlib import Path
from fastapi import APIRouter, File, HTTPException, UploadFile

from app.config import get_settings
from app.services.media import MediaError, detect_kind
from app.schemas import JobSnapshot
from app.deps import container

router = APIRouter(tags=["analyze"])


@router.post("/analyze", response_model=JobSnapshot)
async def create_analysis(file: UploadFile = File(...)):
    filename = file.filename or "upload"
    try:
        kind = detect_kind(Path(filename), file.content_type)
    except MediaError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    job = container.jobs.create(kind=kind, filename=filename)
    target = get_settings().upload_dir / f"{job.id}{Path(filename).suffix.lower()}"

    job.upload_path = target

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
        container.jobs.delete(job.id)
        raise

    job.message = f"File received ({written} bytes)"
    return job.snapshot()

@router.get("/jobs", response_model=list[JobSnapshot])
async def get_jobs():
    return [job.snapshot() for job in container.jobs.list_jobs()]

@router.get("/jobs/{job_id}", response_model=JobSnapshot)
async def get_job(job_id: str):
    job = container.jobs.get(job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return job.snapshot()

@router.delete("/jobs/{job_id}")
async def delete_job(job_id: str):
    job = container.jobs.get(job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    if job.upload_path:
        job.upload_path.unlink(missing_ok=True)
    container.jobs.delete(job_id)
    return {"deleted": job_id}