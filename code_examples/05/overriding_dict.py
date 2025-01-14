# Subclassing `dict``
# With later Python versions use subclassing, not UserDict, UserList, UserString, ...
# or abc collections (see abc.py)


def get_nutrition_information(_text):
    return "arugula"


def get_aliases(text) -> list[str]:
    if text == "rocket":
        return ["arugula"]
    else:
        return []


class NutritionalInformation(dict):
    def __getitem__(self, key):
        try:
            return super().__getitem__(key)
        except KeyError:
            pass
        # not found, try aliases
        for alias in get_aliases(key):
            try:
                return super().__getitem__(alias)
            except KeyError:
                pass
        raise KeyError(f"Could not find {key} or any of its aliases")


if __name__ == "__main__":
    nutrition = NutritionalInformation()
    nutrition["arugula"] = get_nutrition_information("arugula")

    assert nutrition["arugula"] == nutrition["rocket"]  # arugula == rocket
    assert nutrition.get("rocket", "No Key Found") == "No Key Found"  # Uh Oh
