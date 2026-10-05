import asyncio

from app.deps import container
from app.services.pipeline import fake_pipeline


async def main():
    job = container.jobs.create("image", "a.jpg")
    container.spawn(fake_pipeline(job))
    print("right after spawn:", job.status, job.progress, len(container.tasks))
    await asyncio.sleep(2.5)
    print("after 2.5s:", job.status, job.progress, len(container.tasks))
    await asyncio.sleep(3)
    print("after 5.5s:", job.status, job.progress, len(container.tasks))


asyncio.run(main())