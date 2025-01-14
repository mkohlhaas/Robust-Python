from datetime import datetime


def close_kitchen(): ...


def log_time_closed(_point_in_time: datetime): ...


def closing_time() -> datetime: ...


def close_kitchen_if_past_cutoff_time(point_in_time: datetime):
    if point_in_time >= closing_time():
        close_kitchen()
        log_time_closed(point_in_time)
