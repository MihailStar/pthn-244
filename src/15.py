from typing import Callable, TypeVar


def fibonacci(index: int) -> int:
    """@tutorial http://integrator.adior.ru/index.php/robototekhnika/242-python-fibonacci"""

    f0 = 0
    f1 = 1

    for _i in range(index):
        f0, f1 = (f1, f0 + f1)

    return f0


Arg = TypeVar("Arg")
Val = TypeVar("Val")


def caching_decorator(func: Callable[[Arg], Val]) -> Callable[[Arg], Val]:
    cache: dict[Arg, Val] = {}

    def wrapper(arg: Arg) -> Val:
        if arg in cache:
            return cache[arg]

        result = func(arg)
        cache[arg] = result

        return result

    return wrapper


print(caching_decorator(fibonacci)(int(input())))
