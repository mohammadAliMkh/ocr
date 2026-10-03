from pathlib import Path

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.services.media import MediaError, detect_kind

router = APIRouter(tags=["analyze"])


@router.post("/analyze")
async def create_analysis(file: UploadFile = File(...)):
    filename = file.filename or "upload"
    try:
        kind = detect_kind(Path(filename), file.content_type)
    except MediaError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return {"filename": filename, "content_type": file.content_type, "kind": kind}