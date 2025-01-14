from random import choice
from typing import Literal, Optional


class HotDog:
    def add_condiments(self, *_args):
        return None


class Bun:
    def add_frank(self, *_args) -> HotDog:
        return HotDog()


# return type not specific enough
def dispense_frank() -> str:
    return "frank"


def dispense_hot_dog() -> HotDog:
    return HotDog()


# def dispense_ketchup():
def dispense_ketchup() -> Literal["Ketchup"]:
    return "Ketchup"


def dispense_mustard() -> Literal["Mustard"]:
    return "Mustard"


def dispense_bun() -> Optional[Bun]:
    if choice([False, True]):
        return None
    else:
        return Bun()


def dispense_hot_dog_to_customer(_hot_dog):
    pass


def print_error_code(msg: str):
    print(msg)


def create_hot_dog():
    bun = dispense_bun()
    if bun is None:
        print_error_code("Bun could not be dispensed")
        return

    frank = dispense_frank()
    hot_dog = bun.add_frank(frank)
    ketchup = dispense_ketchup()
    mustard = dispense_mustard()
    hot_dog.add_condiments(ketchup, mustard)
    dispense_hot_dog_to_customer(hot_dog)
    print("Bun dispensed to customer.")


if __name__ == "__main__":
    create_hot_dog()
