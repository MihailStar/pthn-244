a = int(input())


def f() -> None:
    global a
    a += 10


f()

print(a)
