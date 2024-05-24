from typing import Generic, TypeVar

K = TypeVar("K")
V = TypeVar("V")


class Dictionary(Generic[K, V]):
    _dictionary: dict[K, V]

    def __init__(self, dictionary: dict[K, V]) -> None:
        self._dictionary = dictionary

    def __call__(self, key: K) -> V | None:
        return self._dictionary.get(key)


if __name__ == "__main__":
    code: list[str] = []

    try:
        while data := input():
            code.append(data)
    except EOFError:
        pass

    exec("\n".join(code))
