from itertools import zip_longest


def fill_missing_values(
    values_1: list[int], values_2: list[int]
) -> list[tuple[int, int]]:
    return list(zip_longest(values_1, values_2, fillvalue=1))


if __name__ == "__main__":
    code: list[str] = []

    try:
        while data := input():
            code.append(data)
    except EOFError:
        pass

    exec("\n".join(code))
