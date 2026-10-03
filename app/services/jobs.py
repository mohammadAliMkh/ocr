import time
from uuid import uuid4

from app.schemas import JobSnapshot, JobStatus, MediaKind


class Job:
    def __init__(self, kind: MediaKind, filename: str) -> None:
        self.id = f"job_{uuid4().hex[:12]}"
        self.kind = kind
        self.filename = filename
        self.status: JobStatus = "queued"
        self.progress = 0.0
        self.message = ""
        self.created_at = time.time()

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
