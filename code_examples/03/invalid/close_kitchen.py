from datetime import datetime


def close_kitchen():
    pass


def closing_time():
    return datetime.now()


def log_time_closed(*_args):
    pass


def close_kitchen_if_past_close(point_in_time: datetime):
    if point_in_time >= closing_time():
        close_kitchen()
        log_time_closed(point_in_time)


class CustomDateTime:
    def __init__(self, text):
        pass


# CustomDateTime offers all the same functionality with datetime.datetime.
# We're using it here for it's better logging facilities.
close_kitchen_if_past_close(CustomDateTime("now"))  # no error
