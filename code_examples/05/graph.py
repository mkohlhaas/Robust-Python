from collections import defaultdict
from typing import NewType

Restaurant = NewType("Restaurant", str)
Recipe = NewType("Recipe", str)


class Graph[Node, Edge]:
    def __init__(self):
        self.edges: dict[Node, list[Edge]] = defaultdict(list)

    def add_relation(self, node: Node, to: Edge):
        self.edges[node].append(to)

    def get_relations(self, node: Node) -> list[Edge]:
        return self.edges[node]


restaurants: Graph[Restaurant, Restaurant] = Graph()

recipes: Graph[Recipe, Recipe] = Graph()
recipes.add_relation(Recipe("Pasta Bolognese"), Recipe("Pasta with Sausage and Basil"))

restaurant_dishes: Graph[Restaurant, Recipe] = Graph()
restaurant_dishes.add_relation(Restaurant("Viafores"), Recipe("Pasta Bolognese"))
