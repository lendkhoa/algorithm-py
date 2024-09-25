"""
AWS provides many services for outlier detection. A prototype small service to detect an outlier in an array of n integers is under development.
Given an array of n integers, there are (n - 2) normal numbers and the sum of the (n - 2) numbers originally in this array. 
If a number is neither in the original numbers nor is it their sum, it is an outlier. 
Discover the potential outliers and return the greatest of them.

Note: It is guaranteed that the answer exists.
Function Description
Complete the function getOutlierValue in the editor.
getOutlierValue has the following parameters:
int arr[n]: value of n-2 numbers, their sum, and outlier value
Returns
int: the outlier value
Input:  arr = [4,  1,  3,  16, 2, 10] total: 36 = sum(n-2) + outlier + potential_outlier
              [1, 2, 3, 4, 10, 16]
              [35, 34, 33, 32, 26, 20]
              [32, 35, 33, 20, 34, 26]
Output: 16 
Explanation:
Remove 16: arr - [4, 1, 3, 2, 10]. The sum of [4, 1, 3, 2] is 10, so 16 is a potential outlier. (16 is not an original number nor their sum.)

        
Remove 4: arr - [1, 3, 16, 2, 10]. The sum of [1, 3, 2, 10] is 16, so 4 is a potential outlier.
The outlier is the greater of the two potential outliers, so 16 is the outlier.
"""
from typing import List

def find_greatest_outlier(arr):
    n = len(arr)
    if n < 3:
        return None  # Not enough elements to have outliers

    potential_outliers = []

    for i in range(n):
        # Create a copy of the array without the current element
        subset = arr[:i] + arr[i+1:]
        subset_sum = sum(subset[:-1])  # Sum of all elements except the last one
        
        # Check if the last element of the subset is equal to the sum of the rest
        if subset[-1] == subset_sum:
            potential_outliers.append(arr[i])

    # Return the greatest outlier if any found, otherwise None
    return max(potential_outliers) if potential_outliers else None

# Test the function
arr = [4, 1, 3, 16, 2, 10]
arr = [2, 17, 81, 6, 106, 5]
result = find_greatest_outlier(arr)
print(result)  # Output: 16