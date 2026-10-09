import asyncio
from collections.abc import Coroutine
from typing import Any

from app.config import get_settings
from app.services.jobs import JobStore
from app.services.vision import VisionAnalyzer


class Container:
    def __init__(self) -> None:
        self.jobs = JobStore()
        self.tasks: set[asyncio.Task] = set()
        self.settings = get_settings()
        self.vision = VisionAnalyzer(self.settings)

    def spawn(self, coro: Coroutine[Any, Any, Any]) -> asyncio.Task:
        task = asyncio.create_task(coro)
        self.tasks.add(task)
        task.add_done_callback(self.tasks.discard)
        return task


container = Container()
