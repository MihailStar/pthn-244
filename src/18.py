from functools import wraps
from typing import Callable, TypeVar

Arg = TypeVar("Arg")
Val = TypeVar("Val")


def cache_deco(func: Callable[[Arg], Val]) -> Callable[[Arg], Val]:
    cache: dict[Arg, Val] = {}

    @wraps(func)
    def wrapper(arg: Arg) -> Val:
        if arg in cache:
            return cache[arg]

        result = func(arg)
        cache[arg] = result

        return result

    return wrapper


code: list[str] = []

try:
    while data := input():
        code.append(data)
except EOFError:
    pass

exec("\n".join(code))
