from enum import auto, Enum


class Allergen(Enum):
    FISH = auto()
    SHELLFISH = auto()
    TREE_NUTS = auto()
    PEANUTS = auto()
    GLUTEN = auto()
    SOY = auto()
    DAIRY = auto()


allergens: set[Allergen] = {Allergen.FISH, Allergen.SOY}
