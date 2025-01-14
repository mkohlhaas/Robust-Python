import datetime

from find_workers import WorkerDatabase, find_workers_available_for_time


def get_ratio(*args):
    return 3.0


class Worker:
    pass


open_time = datetime.datetime.now()
db = WorkerDatabase()
workers: list[str] = find_workers_available_for_time(db, open_time)
numbers: list[int] = []
ratio: float = get_ratio(5, 3)

number: int = 0
text: str = "useless"
values: list[float] = [1.2, 3.4, 6.0]
worker: Worker = Worker()
