"""
Count the number of swap to sort an array when only
adjacent swaps are allow.
The number of swaps = the number of inversions in an array.

I: 2314
O: 1234
To count the inversions --> merge sort --> merge, sort
"""

def merge(left: List[int], right: List[int]):
    # [1, 2] [3, 4]
    merged = []
    inversions = 0
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inversions += len(left) - i
            j+=1
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, inversions

def merge_sort(a: List[int]):
    if len(a) <= 1:
        return a, 0
    n = len(a)
    mid = n // 2
    left, left_inv = merge_sort(a[:mid])
    right, right_inv = merge_sort(a[mid:])
    merged, inversion = merge(left, right)

    return inversion + left_inv + right_inv

# -------------------------------------------------------
def merge(a: List[int], b: List[int]):
    merged = []
    inversions = 0
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i])
            i+=1
        else:
            merged.append(b[j])
            inversions += len(a) - i
            j += 1
    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged, inversions

# Time: O(nlogn)
# Space: O(1)
def merge_sort(a: List[int]):
    n = len(a)
    if n <= 1:
        return a, 0
    mid = n // 2
    left, left_inv = merge_sort(a[:mid])
    right, right_inv = merge_sort(b[mid:])
    merged, inversion = merge(left, right)
    return merged, inversion + left_inv + right_inv





