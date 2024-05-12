# Given the array = [0, 14, 18, 33, 36, 39]
# expected output: [0, 14, 33]
# Make a collapse function that detect the overlap indice and return the collapsed index

from typing import List


def collapse(array: List[int], pattern: str) -> List[int]:
    collapsed = []
    n = len(pattern)
    index = 0
    while index < len(array):
        j = index + 1
        while j < len(array) - 1 and array[j] - array[index] <= n:
            j += 1

        print(f"i: {index}, j: {j}")
        if j - index == 1:
            collapsed.append(array[index])
            index += 1
            continue
        else:
            collapsed.append(array[index])
            index = j
            continue

    if len(array) > 1:
        print(collapsed[0 : len(collapsed) - 1])
        return collapsed[0 : len(collapsed) - 1]
    else:
        print(collapsed)
        return collapsed


if __name__ == "__main__":
    collapse([0, 14, 18, 33, 36, 39], "test")
    collapse([0, 14, 18, 33, 36, 39, 40, 44], "test")
    collapse([10], "test")
