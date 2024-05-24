from typing import Callable, Generator, Iterable, Sequence, TypeVar

In = TypeVar("In")


def filter(
    callback: Callable[[In], bool], iterable: Iterable[In]
) -> Generator[In, None, None]:
    for item in iterable:
        if callback(item):
            yield item


func_in: Callable[[int], bool] = eval(input())
seq_in: Sequence[int] = eval(input())

for x in filter(func_in, seq_in):
    print(x)
