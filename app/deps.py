from app.services.jobs import JobStore
import asyncio
from typing import Any, Coroutine


class Container:
    def __init__(self) -> None:
        self.jobs = JobStore()
        self.tasks: set[asyncio.Task] = set()
    
    def spawn(self, coro: Coroutine[Any, Any, Any]) -> asyncio.Task:
        task = asyncio.create_task(coro)
        self.tasks.add(task)
        task.add_done_callback(self.tasks.discard)
        return task


container = Container()