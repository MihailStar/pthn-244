class Circle:
    pi = 3.14

    def calculate_area(self, radius: float) -> float:
        return self.pi * radius**2


if __name__ == "__main__":
    code: list[str] = []

    try:
        while data := input():
            code.append(data)
    except EOFError:
        pass

    exec("\n".join(code))
