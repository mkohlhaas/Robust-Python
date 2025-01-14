# Use subclassing for your own data types, here Set from ABC collections
# I guess this could be done the same way as in `overriding_dict.py`.

# If you are just extending a type, such as adding new methods, you can subclass
# directly from collections such as a list or dictionary.

# If you need to write a more complicated class with the interface of another collec‐
# tion type, use collections.abc. You will need to provide your own storage for
# the data inside the class and implement all required methods, but once you do,
# you can customize that collection to your heart’s content.

import collections
import collections.abc


def get_nutrition_information(_text):
    return "arugula"


def get_aliases(text) -> list[str]:
    if text == "rocket":
        return ["arugula"]
    else:
        return []


class AliasedIngredients(collections.abc.Set):
    def __init__(self, ingredients: set[str]):
        self.ingredients = ingredients

    def __contains__(self, value: str):
        return value in self.ingredients or any(
            alias in self.ingredients for alias in get_aliases(value)
        )

    def __iter__(self):
        return iter(self.ingredients)

    def __len__(self):
        return len(self.ingredients)


if __name__ == "__main__":
    ingredients = AliasedIngredients({"arugula", "eggplant", "pepper"})
    assert ingredients == {"arugula", "eggplant", "pepper"}
    assert len(ingredients) == 3
    assert "arugula" in ingredients
    assert "rocket" in ingredients
    assert "eggplant" in ingredients
    for ingredient in ingredients:
        print(ingredient)
    print(set(ingredients | AliasedIngredients({"salt"})))
    print(list(ingredients | AliasedIngredients({"salt"})))
