from typing import TypeAlias

Key: TypeAlias = int
Сounter: TypeAlias = int
KeyToСounter: TypeAlias = dict[Key, Сounter]


def make_most_common_keys(d: KeyToСounter) -> list[int]:
    return list(
        map(
            lambda item: item[0],
            sorted(d.items(), key=lambda item: item[1], reverse=True),
        )
    )


code: list[str] = []

try:
    while data := input():
        code.append(data)
except EOFError:
    pass

exec("\n".join(code))
