from dataclasses import dataclass
from typing import Literal


@dataclass
class Error:
    error_code: Literal[1, 2, 3, 4, 5]
    disposed_of: bool


@dataclass
class Snack:
    name: Literal["Pretzel", "Hot Dog"]
    condiments: set[Literal["Mustard", "Ketchup"]]


if __name__ == "__main__":
    _ = Error(1, False)
    _ = Error(2, True)
    _ = Snack("Pretzel", {"Mustard"})
    _ = Snack("Pretzel", {"Ketchup"})
    _ = Snack("Pretzel", {"Mustard", "Ketchup"})
    _ = Snack("Hot Dog", {"Ketchup", "Mustard"})

    # wrong states
    # _ = Error(0, False)
    # _ = Snack("Not Valid", set())
    # _ = Snack("Pretzel", {"Mustard", "Relish"})
