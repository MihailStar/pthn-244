from datetime import datetime, timedelta

days, seconds = int(input()), int(input())


def shift_time(days: int, seconds: int) -> tuple[int, int]:
    initial = datetime(2023, 1, 1, 12, 30, 0)
    shifted = initial + timedelta(days=days, seconds=seconds)

    return (shifted.day, shifted.second)


print(shift_time(days, seconds))
