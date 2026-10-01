import logging

from fastapi import APIRouter

router = APIRouter(tags=["system"])

log = logging.getLogger(__name__)


@router.get("/health")
async def health():
    log.info("health check requested.")
    return {"status": "ok"}
