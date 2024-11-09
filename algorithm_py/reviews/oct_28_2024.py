"""
Inversion counte = merge sort -> count = len(a) - i
"""
from typing import List

def merge(a: List[int], b: List[int]):
    merged = []
    inversions = 0
    # Time: O(n) n < m n is length of a
    # Space: O(n+m) store all the elements of a, b
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            merged.append(a[i])
            i+=1
        else:
            merged.append(b[j])
            inversions += len(a) - i
            j += 1
    merged.extend(a[i:])
    merged.extend(b[j:])

    return merged, inversions

def merge_sort(arr):
    print(f'Merge sort this array {arr}')
    n = len(arr)
    # Base case [0], 0
    if n == 1:
        return arr, 0

    mid = n // 2
    # Time: O(nlogn)
    # Space: O(n)

    # recursion to break the arr into smaller arrays
    left, l_inv = merge_sort(arr[:mid])
    right, r_inv = merge_sort(arr[mid:])

    merged, inv = merge(left, right)
    return merged, l_inv + r_inv + inv

sorted_array, inversion_counts = merge_sort([4,1,2,4,5,9,3,11])
print(sorted_array)
print(inversion_counts)
