# https://medium.com/@ramanbazhanau/advanced-type-annotations-in-python-part-2-58e0b756aede
# https://fastapi.tiangolo.com/python-types/#type-hints-with-metadata-annotations

from typing import Annotated

Age = Annotated[int, "value should be between 0 and 120"]


def validate_age(value: Age) -> None:
    _, metadata = Age.__metadata__
    if not (0 <= value <= 120):
        raise ValueError(f"Invalid age. {metadata}")


DateStr = Annotated[str, {"format": "YYYY-MM-DD"}]


def serialize_date(date: datetime.date) -> DateStr:
    format_str = DateStr.__metadata__[1]["format"]
    return date.strftime(format_str)
