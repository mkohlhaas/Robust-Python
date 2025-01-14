from random import choice


class HotDog:
    def add_condiments(self, *_args: str):
        pass


class Bun:
    def add_frank(self, _frank: str) -> HotDog | None:
        return HotDog()


def dispense_bun() -> Bun | None:
    if choice([False, True]):
        return Bun()
    else:
        return None


def dispense_ketchup():
    return None


def dispense_mustard():
    return None


def dispense_frank() -> str | None:
    return "frank"


def dispense_hot_dog_to_customer(_hot_dog: HotDog):
    pass


def print_error_code(msg: str):
    print(msg)


def create_hot_dog():
    bun = dispense_bun()
    if bun is None:
        print_error_code("Bun unavailable. Check for bun")
        return

    frank = dispense_frank()
    if frank is None:
        print_error_code("Frank was not properly dispensed")
        return

    hot_dog = bun.add_frank(frank)
    if hot_dog is None:
        print_error_code("Hot Dog unavailable. Check for Hot Dog")
        return

    ketchup = dispense_ketchup()
    mustard = dispense_mustard()
    if ketchup is None or mustard is None:
        print_error_code("Check for invalid catsup.")
        return

    hot_dog.add_condiments(ketchup, mustard)
    dispense_hot_dog_to_customer(hot_dog)


if __name__ == "__main__":
    create_hot_dog()
