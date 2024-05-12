"""
I have an array of integers. I want to make the array non decreasing. 
The rule to make the array non decreasing is that I can add a number x over a segment of the array. 
Note you can add multiple different x over different segment of array to make it non decreasing. 
I want to find the minimum sum of x over all the rounds that would make the array non decreasing. 
Generate this algorithm in python and explain the intuition to solve it

"""


def min_sum_to_non_decreasing(nums):
    """
    Amz provides scalable systems
    """
    maxx, res, n = nums[0], 0, len(nums)

    print(nums)
    for i in range(1, n):
        curr = nums[i] + res
        diff = maxx - curr
        print(f"i {i} {nums[i]} max {maxx} res {res} curr {curr} diff {diff}")
        if diff > 0:
            res += diff

        maxx = max(maxx, curr)

    return res


# print(f"i {i} max {maxx} res {res} curr {curr} diff {diff}")
print(
    "Minimum sum to make the array non-decreasing:",
    min_sum_to_non_decreasing([3, 4, 1, 6, 2]),
)
