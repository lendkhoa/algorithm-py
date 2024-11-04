"""
Inversion count = number of swaps to sort the array
merge sort
"""
from typing import List

# Time: O(n) n is length of n (n > m)
# Space: O(n+m)
def merge(list1: List[int], list2: List[int]) -> List[int]:
    merged = []
    i, j = 0, 0
    inversions = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i+=1
        else:
            merged.append(list2[j])
            inversions += len(list1) - i
            j += 1
    merged.extend(list1[:i])
    merged.extend(list2[:j])

    return merged, inversions

def merge_sort(arr: List[int]):
    n = len(arr)
    if n <= 1:
        return arr, 0

    mid = n // 2
    left, left_inv = merge_sort(a[:mid])
    right, right_inv = merge_sort(a[mid:])
    merged, inversions = merge(left, right)

    return inversions + left_inv + right_inv
