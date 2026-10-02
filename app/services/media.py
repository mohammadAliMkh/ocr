from pathlib import Path

from app.schemas import MediaKind

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tif", ".tiff"}
VIDEO_EXTENSIONS = {".mp4", ".mov", ".mkv", ".avi", ".webm"}


class MediaError(Exception):
    pass


def detect_kind(
    path: Path,
    content_type: str | None = None,
) -> MediaKind:
    suffix = path.suffix.lower()

    if suffix in VIDEO_EXTENSIONS:
        return "video"

    if suffix in IMAGE_EXTENSIONS:
        return "image"

    if content_type:
        if content_type.startswith("video/"):
            return "video"

        if content_type.startswith("image/"):
            return "image"

    raise ValueError(f"Unsupported media type: {suffix or content_type or 'unknown'}")
