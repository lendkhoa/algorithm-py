"""
Quick select. k-th largest
"""

# Find the kth smallest elements
def quickSelect(arr, k):
    if len(arr) == 1:
        return arr[0]
    
    # pick the middle element
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    if k <= len(left):
        return quickSelect(left, k)
    elif k <= len(left) + len(middle):
        # All elements in left are smaller than pivot
        # All elements in right are larger than pivot
        # So pivot must be the kth element if k is equal to the number of elements smaller than or equal to pivot
        return pivot
    else:
        # This adjustment of k is necessary because we're now searching in a smaller array (right) but still want to maintain the correct position relative to the original array.
        return quickSelect(right, k - len(left) - len(middle))

# Find the kth largest
# Convert kth largest to (n-k+1)th smallest