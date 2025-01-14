from collections import defaultdict
from dataclasses import dataclass

type Author = str
type Number_of_Books = int


@dataclass
class Cookbook:
    author: Author


def create_author_count_mapping(cookbooks: list[Cookbook]):
    counter: dict[Author, Number_of_Books] = defaultdict(lambda: 0)
    for cookbook in cookbooks:
        counter[cookbook.author] += 1
    return counter


def test_create_author_count():
    cookbooks = [
        Cookbook("Pat Viafore"),
        Cookbook("Pat Viafore"),
        Cookbook("J. Kenji Lopez-Alt"),
    ]
    assert create_author_count_mapping(cookbooks) == {
        "Pat Viafore": 2,
        "J. Kenji Lopez-Alt": 1,
    }


test_create_author_count()
