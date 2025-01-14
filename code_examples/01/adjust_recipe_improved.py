from dataclasses import dataclass
from fractions import Fraction


@dataclass
class Ingredient:
    name: str
    amount: Fraction
    units: str

    def adjust_proportion(self, factor: Fraction):
        self.amount *= factor


@dataclass
class Recipe:
    servings: int
    ingredients: list[Ingredient]

    def clear_ingredients(self):
        self.ingredients.clear()

    def get_ingredients(self):
        return self.ingredients


# Take a meal recipe and change the number of servings.
def adjust_recipe(recipe: Recipe, servings: int):
    new_ingredients = list(recipe.get_ingredients())  # create a copy of the ingredients
    recipe.clear_ingredients()
    for ingredient in new_ingredients:
        ingredient.adjust_proportion(Fraction(servings, recipe.servings))
    return Recipe(servings, new_ingredients)


def test_adjust_recipe():
    old_recipe = Recipe(2, [Ingredient("flour", Fraction(3, 2), "cups")])
    adjusted = adjust_recipe(old_recipe, 4)
    assert Recipe(4, [Ingredient("flour", Fraction(3), "cups")]) == adjusted
    assert old_recipe.ingredients == []


test_adjust_recipe()
