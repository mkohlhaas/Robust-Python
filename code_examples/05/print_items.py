from collections.abc import Iterable


def print_items(items: Iterable):
    for item in items:
        print(item)


print_items("abc")
print_items([1, 2, 3, 4])
print_items({5, 3, 4})
