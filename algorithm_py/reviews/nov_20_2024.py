"""
Combination sum II
In: An array of integers and target.
Out: A list of all unique combinations of candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.
Example:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
"""
from typing import List

def combination_sum_II(candidates: List[int], target: int) -> List[List[int]]:
    result = set()
    # using current_total to keep track of latest count. Don't have to call sum

    def backtrack(i, subset, current_total):
        # exit condition
        if i >= len(candidates) or current_total > target:
            return        
        if current_total == target:
            result.add(tuple(subset))
            return
        subset.append(candidates[i])
        # we don't want duplicate
        backtrack(i+1, subset, current_total + candidates[i]) 
        subset.pop()
        backtrack(i+1, subset, current_total)
    
    backtrack()
    return [list(s) for s in result]

"""
⭐️ The number of candidate can be duplicated
You are given an array of distinct integers nums and a target integer target. Your task is to return a list of all unique combinations of nums where the chosen numbers sum to target.

The same number may be chosen from nums an unlimited number of times. Two combinations are the same if the frequency of each of the chosen numbers is the same, otherwise they are different.

You may return the combinations in any order and the order of the numbers in each combination can be in any order.

"""

def combination_sum(nums: List[int], target: int) -> List[List[int]]:
    result = []
    def backtrack(i, subset, current_total):
        if current_total == target:
            result.append(subset.copy())
            return
        if i >= len(nums) or current_total > target:
            return
        subset.append(nums[i])
        backtrack(i, subset, current_total + nums[i])
        subset.pop()
        backtrack(i+1, subset, current_total)

    backtrack(0, [], 0)
    return result
