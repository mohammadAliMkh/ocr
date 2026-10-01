import logging

from fastapi import FastAPI

from app import config
from app.logging_setup import setup_logging
from app.routers import health

settings = config.get_settings()

setup_logging(settings.log_level)
log = logging.getLogger(__name__)

settings.build()

log.info("Data directory: %s", settings.data_dir)

app = FastAPI(title=settings.app_name, version=settings.app_version)


@app.get("/")
def root():
    return {"app": settings.app_name, "version": settings.app_version, "docs": "/docs"}


app.include_router(health.router, prefix="/api")
