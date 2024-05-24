from collections import Counter
from datetime import datetime


def most_common_months(dates: list[str], n: int) -> list[int]:
    return list(
        map(
            lambda month_and_count: month_and_count[0],
            Counter(
                map(
                    lambda date: datetime.strptime(date, "%Y-%m-%dT%H:%M:%S").month,
                    dates,
                )
            ).most_common(n),
        )
    )


if __name__ == "__main__":
    code: list[str] = []

    try:
        while data := input():
            code.append(data)
    except EOFError:
        pass

    exec("\n".join(code))
