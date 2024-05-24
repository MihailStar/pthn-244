from __future__ import annotations


class Rectangle:
    a: float
    b: float

    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b

    def calculate_area(self) -> float:
        return self.a * self.b


class Square(Rectangle):
    def __init__(self, a: float) -> None:
        super().__init__(a, a)


class CalculatePerimeterMixin(Rectangle):
    def calculate_perimeter(self) -> float:
        return 2 * (self.a + self.b)


class SquareWithMixin(CalculatePerimeterMixin, Square):
    def __eq__(self, other: object) -> bool:
        return isinstance(other, Square) and self.a == other.a and self.b == other.b

    def __gt__(self, other: Square) -> bool:
        return self.calculate_area() > other.calculate_area()

    def __add__(self, other: Square) -> float:
        return self.calculate_area() + other.calculate_area()


if __name__ == "__main__":
    code: list[str] = []

    try:
        while data := input():
            code.append(data)
    except EOFError:
        pass

    exec("\n".join(code))
