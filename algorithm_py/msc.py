# The numbers are not sorted. Can be negative
# 3sum = target
from typing import List

def threeSumWithTarget(nums: List[int], target: int) -> List[List[int]]:
    res = []
    def twoSum(start: int):
        nonlocal nums
        nonlocal res
        nonlocal target

        lo, hi = start + 1, len(nums) - 1

        while lo < hi:
            sum = nums[start] + nums[lo] + nums[hi]
            if sum == target:
                res.append([nums[start], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                # skip the duplicate
                while lo < hi and nums[lo-1] == nums[lo]:
                    lo += 1 
            elif sum > target:
                hi -= 1
            else:
                lo += 1
        print(f'  {res}')

    nums.sort()
    print(f'sorted: {nums}')
    for i in range(len(nums)):
        if i == 0 or nums[i - 1] != nums[i]: # skip the duplicate
            print(f' i: {i} {nums[i]}')
            twoSum(i)
    
    return res

# print(threeSumWithTarget([-1,0,1,2,-1,-4], 0))
# print(threeSumWithTarget([-1,0,1,2,-1,-4], 3))
print(threeSumWithTarget([1,2,-2,-1], 0))