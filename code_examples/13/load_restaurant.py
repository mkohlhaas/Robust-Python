from typing import Protocol

import restaurant


class Restaurant(Protocol):
    name: str
    address: str
    standard_lunch_entries: list[str]
    other_entries: list[str]

    def render_menu(self) -> str: ...


def load_restaurant(_restaurant: Restaurant):
    # code to load restaurant
    # ...
    pass


if __name__ == "__main__":
    # mypy does not support modules as protocols yet
    load_restaurant(restaurant)  # type: ignore
