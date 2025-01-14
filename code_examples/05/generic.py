# from typing import TypeVar

# T = TypeVar("T")


class NutritionInfo:
    pass


class Ingredient:
    pass


class Restaurant:
    pass


class APIErrorResponse:
    pass


type APIResponse[T] = T | APIErrorResponse


def get_nutrition_info(_recipe: str) -> APIResponse[NutritionInfo]:
    return APIErrorResponse()


def get_ingredients(_recipe: str) -> APIResponse[list[Ingredient]]:
    return []


def get_restaurants_serving(_recipe: str) -> APIResponse[list[Restaurant]]:
    return [Restaurant()]
