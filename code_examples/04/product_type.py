from dataclasses import dataclass


@dataclass
class Snack:
    name: str
    condiments: set[str]
    error_code: int  # should be enum, class, ...
    disposed_of: bool


Snack("Hotdog", {"Mustard", "Ketchup"}, 5, False)
