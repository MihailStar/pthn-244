from typing import Callable, Generator, Iterable, Sequence, TypeVar

In = TypeVar("In")
Out = TypeVar("Out")


def map(
    callback: Callable[[In], Out], iterable: Iterable[In]
) -> Generator[Out, None, None]:
    for item in iterable:
        yield callback(item)


func_in: Callable[[int], int] = eval(input())
seq_in: Sequence[int] = eval(input())

for x in map(func_in, seq_in):
    print(x)
