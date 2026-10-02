from typing import Literal

from pydantic import BaseModel, Field

MediaKind = Literal["image", "video"]

JobStatus = Literal["queued", "running", "done", "error"]


class JobSnapshot(BaseModel):
    id: str
    filename: str
    kind: MediaKind
    status: JobStatus
    progress: float = Field(ge=0, le=1)
    message: str
