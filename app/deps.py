import asyncio
from collections.abc import Coroutine
from typing import Any

from app.config import get_settings
from app.services.jobs import JobStore
from app.services.vision import VisionAnalyzer
from app.services.vlm import VLMClient

import logging

log = logging.getLogger(__name__)


class Container:
    def __init__(self) -> None:
        self.jobs = JobStore()
        self.tasks: set[asyncio.Task] = set()
        self.settings = get_settings()
        self.vision = VisionAnalyzer(self.settings)
        self.vlm = VLMClient(self.settings)

    def spawn(self, coro: Coroutine[Any, Any, Any]) -> asyncio.Task:
        task = asyncio.create_task(coro)
        self.tasks.add(task)
        task.add_done_callback(self.tasks.discard)
        return task
    
    async def shutdown(self) -> None:
        tasks = list(self.tasks)

        for task in tasks:
            task.cancel()

        await asyncio.gather(*tasks, return_exceptions=True)
        log.info("Cancelled %d background tasks", len(tasks))

        await self.vlm.aclose()
        log.info("VLM client closed")


container = Container()
