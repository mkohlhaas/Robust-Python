import random
from datetime import datetime

OWNER = "Pat"


class WorkerDatabase:
    def get_all_workers(self) -> list[str]:
        return []


def get_emergency_workers() -> list[str]:
    return []


def is_available(_name: str) -> bool:
    return True


def find_workers_available_for_time(
    db: WorkerDatabase, _open_time: datetime
) -> list[str]:
    workers = db.get_all_workers()
    available_workers = [worker for worker in workers if is_available(worker)]
    if available_workers:
        return available_workers

    # fall back to workers who listed they are available in
    # in an emergency
    emergency_workers = [
        worker for worker in get_emergency_workers() if is_available(worker)
    ]

    if emergency_workers:
        return emergency_workers

    # Schedule the owner to open, they will find someone else
    return [OWNER]


# functions with side-effects (return type = None)
def schedule(_worker, _open_time):
    pass


def schedule_restaurant_open(
    db: WorkerDatabase, open_time: datetime, num_workers_needed: int
):
    workers = find_workers_available_for_time(db, open_time)
    # use random.sample to pick X available workers
    # where X is the number of workers needed.
    for worker in random.sample(workers, num_workers_needed):
        schedule(worker, open_time)


if __name__ == "__main__":
    db = WorkerDatabase()
    assert find_workers_available_for_time(db, datetime.now()) == ["Pat"]
