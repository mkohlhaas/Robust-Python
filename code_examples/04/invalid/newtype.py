from typing import NewType


class HotDog:
    def add_condiments(self, *_args):
        pass


class Bun:
    def add_frank(self, frank: str) -> HotDog:
        print(f"Adding frank: {frank}")
        return HotDog()


ReadyToServeHotDog = NewType("ReadyToServeHotDog", HotDog)


def dispense_bun() -> Bun:
    return Bun()


def dispense_ketchup():
    return None


def dispense_mustard():
    return None


def dispense_hot_dog_to_customer(_hot_dog: HotDog):
    pass


def dispense_frank() -> str:
    return "Frank"


def serve_to_customer(*_args: ReadyToServeHotDog):
    pass


def create_hot_dog():
    bun = dispense_bun()
    frank = dispense_frank()
    hot_dog = bun.add_frank(frank)
    ketchup = dispense_ketchup()
    mustard = dispense_mustard()
    hot_dog.add_condiments(ketchup, mustard)
    dispense_hot_dog_to_customer(hot_dog)


if __name__ == "__main__":
    serve_to_customer(ReadyToServeHotDog(HotDog()))
    print("Hotdog served!")
