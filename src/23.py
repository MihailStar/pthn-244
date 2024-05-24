def get_indexes(nums1: list[int], nums2: list[int]) -> list[int]:
    indexs: list[int] = []

    for index, [num1, num2] in enumerate(zip(nums1, nums2)):
        if num1 < num2:
            indexs.append(index)

    return indexs


code: list[str] = []

try:
    while data := input():
        code.append(data)
except EOFError:
    pass

exec("\n".join(code))
