"""
Program to count the number of swaps (inversions) to sort an array
when only swapping of adjacent elements are allowed
"""
from typing import List

def merge_sort(arr: List[int]):
    print(f'Merge sort on {arr}')
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    print(f' mid: {mid}')
    left, left_inv = merge_sort(arr[:mid])
    right, right_inv = merge_sort(arr[mid:])
    merged, merge_inv = merge(left, right)

    return merged, left_inv + right_inv + merge_inv

def merge(left: List[int], right: List[int]):
    merged = []
    inversions = 0
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            # the current value at j is larger than left
            #  0 1   0 1
            # [2,3] [1,4]
            merged.append(right[j])
            inversions += len(left) - i
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, inversions

# print(merge([2, 3], [1, 4]))
print(merge_sort([1,2,4,4,1,1,5,7]))
