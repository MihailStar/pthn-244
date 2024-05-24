class Circle:
    _pi = 3.14

    def __init__(self, radius: float) -> None:
        self._radius = radius

    @property
    def radius(self) -> float:
        return self._radius

    @property
    def pi(self) -> float:
        return self._pi

    def calculate_area(self) -> float:
        return self._pi * self._radius**2


class CalculateCircleLengthMixin:
    def calculate_length(self) -> float:
        return 2 * super().pi * super().radius  # type: ignore


class CircleWithMixin(CalculateCircleLengthMixin, Circle):
    pass


if __name__ == "__main__":
    code: list[str] = []

    try:
        while data := input():
            code.append(data)
    except EOFError:
        pass

    exec("\n".join(code))
