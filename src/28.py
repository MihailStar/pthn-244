class Pendulum:
    g = 10
    pi = 3.14

    @classmethod
    def calculate_period(cls, length: int) -> float:
        return 2 * cls.pi * (length / cls.g) ** 0.5


if __name__ == "__main__":
    code: list[str] = []

    try:
        while data := input():
            code.append(data)
    except EOFError:
        pass

    exec("\n".join(code))
