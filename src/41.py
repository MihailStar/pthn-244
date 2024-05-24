from collections import deque


def rotate_list(nums: list[int], n: int) -> list[int]:
    queue = deque(nums)

    for _ in range(n):
        queue.appendleft(queue.pop())

    return list(queue)


if __name__ == "__main__":
    code: list[str] = []

    try:
        while data := input():
            code.append(data)
    except EOFError:
        pass

    exec("\n".join(code))
