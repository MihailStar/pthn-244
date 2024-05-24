from collections import defaultdict
from typing import TypeVar

Speciality = TypeVar("Speciality")
Name = TypeVar("Name")


def fill_specializations(
    specializations: list[tuple[Speciality, Name]]
) -> dict[Speciality, list[Name]]:
    speciality_to_names: defaultdict[Speciality, list[Name]] = defaultdict(list)

    for speciality, name in specializations:
        speciality_to_names[speciality].append(name)

    return dict(speciality_to_names)


if __name__ == "__main__":
    code: list[str] = []

    try:
        while data := input():
            code.append(data)
    except EOFError:
        pass

    exec("\n".join(code))
