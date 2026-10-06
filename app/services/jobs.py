import time
from uuid import uuid4

from app.schemas import JobSnapshot, JobStatus, MediaKind

from pathlib import Path

import asyncio


class Job:
    def __init__(self, kind: MediaKind, filename: str) -> None:
        self.id = f"job_{uuid4().hex[:12]}"
        self.kind = kind
        self.filename = filename
        self.status: JobStatus = "queued"
        self.progress = 0.0
        self.message = ""
        self.created_at = time.time()
        self.upload_path: Path | None = None
        self.events: list[dict] = []
        self._subscribers: set[asyncio.Queue] = set()

    def publish(self, event_type: str, **data) -> None:
        event = {"type": event_type, "ts": time.time(), **data}
        self.events.append(event)
        for queue in self._subscribers:
            queue.put_nowait(event)

    def set_progress(self, value: float, message: str = "") -> None:
        self.progress = max(0.0, min(1.0, value))
        if message:
            self.message = message
        self.publish("progress", progress=self.progress, message=self.message)

    def finish(self, message: str = "Analysis complete") -> None:
        self.status = "done"
        self.progress = 1.0
        self.message = message
        self.publish("done", message=self.message)

    def fail(self, error: str) -> None:
        self.status = "error"
        self.message = error
        self.publish("error", message=error)

    async def subscribe(self):
        queue: asyncio.Queue = asyncio.Queue()
        self._subscribers.add(queue)
        try:
            while True:
                event = await queue.get()
                yield event
                if event["type"] in ("done", "error"):
                    return
        finally:
            self._subscribers.discard(queue)       

    def snapshot(self) -> JobSnapshot:
        return JobSnapshot(
            id=self.id,
            filename=self.filename,
            kind=self.kind,
            status=self.status,
            progress=self.progress,
            message=self.message,
            created_at=self.created_at,
        )


class JobStore:
    def __init__(self) -> None:
        self._jobs: dict[str, Job] = {}

    def create(self, kind: MediaKind, filename: str) -> Job:
        job = Job(kind=kind, filename=filename)
        self._jobs[job.id] = job
        return job

    def get(self, job_id: str) -> Job | None:
        return self._jobs.get(job_id)

    def list_jobs(self) -> list[Job]:
        return list(reversed(self._jobs.values()))

    def delete(self, job_id: str) -> bool:
        return self._jobs.pop(job_id, None) is not None
