def handle(string: str) -> str:
    return (
        (string.upper() if string.startswith("!") else string.lower())
        .replace("!", "")
        .replace("@", "")
        .replace("#", "")
        .replace("%", "")
    )


def main() -> None:
    try:
        for string in iter(input, ""):
            print(handle(string))
    except EOFError:
        pass


main()
