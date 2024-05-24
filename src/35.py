numerator, denominator = int(input()), int(input())


def changed_div(numerator: int, denominator: int) -> float:
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return numerator


print(changed_div(numerator, denominator))
