print(
    *map(
        lambda num: -num if num % 2 == 0 else num**2,
        range(*map(int, input().split())),
    ),
    sep="\n"
)
