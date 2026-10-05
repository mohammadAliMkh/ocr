from app.services.jobs import JobStore


class Container:
    def __init__(self) -> None:
        self.jobs = JobStore()


container = Container()