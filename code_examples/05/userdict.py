# Using UserDict instead of just `dict`

from collections import UserDict


def get_nutrition_information(_text):
    return "arugula"


def get_aliases(text) -> list[str]:
    if text == "rocket":
        return ["arugula"]
    else:
        return []


class NutritionalInformation(UserDict):
    def __getitem__(self, key):
        try:
            return self.data[key]
        except KeyError:
            pass
        # not found, try aliases
        for alias in get_aliases(key):
            try:
                return self.data[alias]
            except KeyError:
                pass
        raise KeyError(f"Could not find {key} or any of its aliases")


if __name__ == "__main__":
    nutrition = NutritionalInformation()
    nutrition["arugula"] = get_nutrition_information("arugula")

    assert nutrition["arugula"] == nutrition["rocket"]

    # `get` doesn't call our __getitem__ method!
    # assert (
    #     nutrition.get("rocket", "No Key Found") == nutrition["arugula"]
    # )
