import logging

from fastapi import APIRouter

from app.config import get_settings
from app.deps import container

router = APIRouter(tags=["system"])

log = logging.getLogger(__name__)


@router.get("/config")
async def get_config():
    return get_settings().public_snapshot()


@router.get("/health")
async def health():
    log.info("health check requested.")
    return {
        "status": "ok",
        "vision": container.vision.status(),
    }
