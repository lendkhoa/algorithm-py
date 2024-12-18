"""
Permutation
Given an array of unique integers. Return all possible permutation.
Ex1:
nums = [1,2,3]
[[1,2,3], [1,3,2], [2, 1, 3]]
"""
from typing import List
def permutation(nums: List[int]):
  res = []
  backtrack([], nums, res, [False] * len(nums))
  return res

# 1 array to keep trakck of the permutation
# the return result
# :another array to keep track of which one we have picked
def backtrack(permutation: List[int], nums: List[int], res: List[int], pick: List[bool]):
  if len(permutation) == len(nums):
    res.append(permutation[:])
    return
  for i in range(len(nums)):
    if not pick[i]:
      permutation.append(nums[i])
      pick[i] = True
      backtrack(permutation, nums, res, pick)
      permutation.pop()
      pick[i] = False

def test():
  nums = [1,2,3]
  print(permutation(nums))

test()