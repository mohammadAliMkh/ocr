import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import config
from app.logging_setup import setup_logging
from app.routers import health, analyze

settings = config.get_settings()

setup_logging(settings.log_level)
log = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):

    settings.build()

    log.info("Starting %s v%s", settings.app_name, settings.app_version)
    log.info("Data directory: %s", settings.data_dir)

    yield

    log.info("Shutdown complete")


app = FastAPI(title=settings.app_name, version=settings.app_version, lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_list,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"app": settings.app_name, "version": settings.app_version, "docs": "/docs"}


app.include_router(health.router, prefix="/api")

app.include_router(analyze.router, prefix="/api")
