from typing import Generic, TypeVar

K = TypeVar("K")
V = TypeVar("V")


class ContextDictionary(Generic[K, V]):
    dictionary: dict[K, V] | None

    def __init__(self) -> None:
        self.dictionary = None

    def __enter__(self) -> None:
        self.dictionary = dict()

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:  # type: ignore
        self.dictionary = None

    def put(self, key: K, value: V) -> None:
        self.dictionary[key] = value  # type: ignore

    def get(self, key: K) -> V:
        return self.dictionary[key]  # type: ignore


if __name__ == "__main__":
    code: list[str] = []

    try:
        while data := input():
            code.append(data)
    except EOFError:
        pass

    exec("\n".join(code))
