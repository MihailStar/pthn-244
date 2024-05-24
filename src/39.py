from datetime import datetime, timedelta

string_datetime = input()


def parse_time(string: str) -> int:
    parsed = datetime.strptime(string, "%Y %m %d %H %M %S")
    shifted = parsed + timedelta(days=1)

    return shifted.day


print(parse_time(string_datetime))
