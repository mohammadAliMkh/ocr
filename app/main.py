from fastapi import FastAPI
from app.routers import health

app = FastAPI(title="OCR APP" , version="1.0.0")

@app.get("/")
def root():
    return {"message":"OCR Application"}


app.include_router(
    health.router,
    prefix="/api"
)