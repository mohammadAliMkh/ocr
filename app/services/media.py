from pathlib import Path

from app.schemas import MediaKind

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tif", ".tiff"}
VIDEO_EXTENSIONS = {".mp4", ".mov", ".mkv", ".avi", ".webm"}


class MediaError(Exception):
    pass


def detect_kind(path: Path) -> MediaKind:
    suffix = path.suffix.lower()

    if suffix in VIDEO_EXTENSIONS:
        return "video"

    if suffix in IMAGE_EXTENSIONS:
        return "image"

    raise MediaError(f"Unsupported file type: {suffix or 'unknown'}")
