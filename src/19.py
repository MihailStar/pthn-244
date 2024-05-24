from functools import wraps
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def repeat_deco(n: int = 1) -> Callable[[Callable[P, R]], Callable[P, R]]:
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            result = func(*args, **kwargs)

            for _ in range(n - 1):
                result = func(*args, **kwargs)

            return result

        return wrapper

    return decorator


code: list[str] = []

try:
    while data := input():
        code.append(data)
except EOFError:
    pass

exec("\n".join(code))
