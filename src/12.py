def get_average(sequence: str, /) -> float:
    digits = sequence.split()
    numbers = list(map(int, digits))
    average = sum(numbers) / len(numbers)

    return average


def main() -> None:
    try:
        for sequence in iter(input, ""):
            print(round(get_average(sequence), 2))
    except EOFError:
        pass


main()
