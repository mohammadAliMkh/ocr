import asyncio
import logging

from app.services.jobs import Job

log = logging.getLogger(__name__)

async def fake_pipeline(job: Job) -> None:
    try:
        job.status = "running"
        for step in range(1, 6):
            await asyncio.sleep(4)
            job.progress = step / 5
            job.message = f"Step {step}/5"
        job.status = "done"
        job.message = "Analysis complete"
        log.info("Job %s done", job.id)
    except Exception as exc:
        log.exception("Job %s failed", job.id)
        job.status = "error"
        job.message = f"{type(exc).__name__}: {exc}"