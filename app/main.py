from fastapi import FastAPI
from app.routers import health
from app import config

settings = config.get_settings()

app = FastAPI(title=settings.app_name , version=settings.app_version)

@app.get("/")
def root():
    return {
        "app":settings.app_name,
        "version":settings.app_version,
        "docs":"/docs"
    }


app.include_router(
    health.router,
    prefix="/api"
)