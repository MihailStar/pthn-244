from functools import wraps
from typing import Callable, Generator, Iterable, TypeVar

A = TypeVar("A")
V = TypeVar("V")


def cache_deco(func: Callable[[A], V]) -> Callable[[A], V]:
    cache: dict[A, V] = {}

    @wraps(func)
    def wrapper(arg: A) -> V:
        if arg in cache:
            return cache[arg]

        result = func(arg)
        cache[arg] = result

        return result

    return wrapper


T = TypeVar("T")
R = TypeVar("R")


def solution(
    func_map: Callable[[T], R], func_filter: Callable[[T], bool], data: Iterable[T]
) -> Generator[R, None, None]:
    for index, item in enumerate(map(func_map, filter(func_filter, data))):
        if index % 2 == 0:
            yield item


if __name__ == "__main__":
    code: list[str] = []

    try:
        while data := input():
            code.append(data)
    except EOFError:
        pass

    exec("\n".join(code))
