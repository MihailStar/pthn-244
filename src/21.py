def g() -> None:
    b = int(input())

    def h() -> None:
        nonlocal b
        b += 10

    h()

    print(b)


g()
