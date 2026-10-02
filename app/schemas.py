from typing import Literal

from pydantic import BaseModel

MediaKind = Literal["image", "video"]

JobStatus = Literal["queued", "running", "done", "error"]


class JobSnapshot(BaseModel):
    id: str
    filename: str
    kind: MediaKind
    status: JobStatus
    progress: float
    message: str
