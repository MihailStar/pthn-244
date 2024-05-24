class Counter:
    _value: int

    def __init__(self, initial_count: int) -> None:
        self._value = initial_count

    def increment(self) -> None:
        self._value += 1

    def get(self) -> int:
        return self._value


if __name__ == "__main__":
    code: list[str] = []

    try:
        while data := input():
            code.append(data)
    except EOFError:
        pass

    exec("\n".join(code))
