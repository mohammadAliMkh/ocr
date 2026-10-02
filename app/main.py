import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app import config
from app.logging_setup import setup_logging
from app.routers import health


@asynccontextmanager
async def lifespan(app: FastAPI):
    # این‌جا: موقع روشن شدن
    settings = config.get_settings()
    settings.build()

    setup_logging(settings.log_level)
    log = logging.getLogger(__name__)
    log.info(
        "Starting %s v%s",
        settings.app_name,
        settings.app_version,
    )
    log.info("Data directory: %s", settings.data_dir)

    yield
    # این‌جا: موقع خاموش شدن
    log.info("Shutdown complete")


app = FastAPI(lifespan=lifespan)


@app.get("/")
def root():
    settings = config.get_settings()
    return {"app": settings.app_name, "version": settings.app_version, "docs": "/docs"}


app.include_router(health.router, prefix="/api")
