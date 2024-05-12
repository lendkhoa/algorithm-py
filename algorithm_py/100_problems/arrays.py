from typing import List


def move_negative_to_front(nums: List[int]) -> List[int]:
    """
    Returns the array with negative number at the front
    retaining the order
    Input will be:
    2 -9 10 12 5 -2 10 -4
    Output will be:
    -9 -2 -4 2 10 12 5 10

    Ideas: 2 pointers L-R. All ele before L is negative, All ele after R is positive

    Worst case time complexity: Θ(k), where k is the number of negative elements
    This occurs when all negative elements occur after the positive elements.
    All negative elements need to be swapped over to the front of the array.

    Average case time complexity: O(N/2)
    On average, by probabilistic analysis, about N/2 negative numbers lie to the right of left pointer and need to be swapped over.

    Best case time complexity: Θ(1)
    This occurs when the elements are already in the correct order and do not require any rearranging.
    Space complexity: Θ(1)

    Shortcomings: Since 0 is neither a negative or positive number,
    the algorithm fails to place it at the right spot and it may land either in the negative or positive halves
    """
    l = 0
    r = len(nums) - 1
    while l < r:
        left_ele = nums[l]
        right_ele = nums[r]
        if left_ele < 0 and right_ele < 0:
            # Both are negative
            l += 1
        elif left_ele > 0 and right_ele < 0:
            # Left is positive, right is negative
            nums[l] = right_ele
            nums[r] = left_ele
            l += 1
            r -= 1
        elif left_ele > 0 and right_ele > 0:
            # Both are positive
            r -= 1
        else:
            l += 1
            r -= 1
    return nums


def move_negatives_to_back(nums: List[int]) -> List[int]:
    print(f"\n Move negatives to back of array | input {nums} \n")
    """
    2 pointers: left, right
    before Left (positive)
    after Right (negative)
                both negative | l<0, r>0
    -2 3 1 -1 |-2 3 1 -1 | 1 3 -2 -1
    |       r | l   r    |   lr

    -2 3 3

    Time: O(N/2) -> O(N)
    Space: O(1)
    """
    left = 0
    right = len(nums) - 1
    while left < right:
        left_ele = nums[left]
        right_ele = nums[right]
        if left_ele < 0 and right_ele < 0:
            right -= 1
        elif left_ele < 0 and right_ele > 0:
            nums[right] = left_ele
            nums[left] = right_ele
            left += 1
            right -= 1
        elif left_ele > 0 and right_ele > 0:
            left += 1
        else:
            left += 1
            right -= 1
    return nums


def makeAnagram(a, b):
    """
    Given two strings. Returns an integer representing the minimum
    total characters that must be deleted to make the strings anagrams
    """
    # instead of counting the number of character
    # we must delete, we replace the characters
    # that both a, b share
    for char in b:
        if char in a:
            a = a.replace(char, "", 1)
            b = b.replace(char, "", 1)
    return len(a) + len(b)


def rotate_array(arr, n):
    """
    Left rotate of the array by n
    """
    n = n % len(arr)
    print(f"Rotating {arr} | n: {n} step(s) to the left")
    result = []
    for i in range(len(arr)):
        result.append(arr[(i + n) % len(arr)])

    print(f"Rotated array: {result}")
    return result


def rotate_array_right(nums, n):
    print(f"Rotating array {nums} to the right {n} step")
    """
    Rotating to the right k step is the
    same as rotating to the left n - k steps
    """
    n = (len(nums) - n) % len(nums)
    result = []
    for i in range(len(nums)):
        result.append(nums[(i + n) % len(nums)])

    print(f"Rotated array: {result}")
    return result


def three_closest_sum_variation_1(nums: List[int], target: int) -> int:
    """
    Given an array of integer numbers. Find three integers in nums such that the sum is
    closest to 'target'. RETURN the SUM of the three integers
    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    diff = float("inf")
    nums.sort()  # nlogn sort in ascending order
    n = len(nums)
    res = [-1, -1, -1]
    for i in range(n):
        l = i + 1
        h = n - 1
        while l < h:
            sum = nums[i] + nums[l] + nums[h]
            if abs(target - sum) < abs(diff):
                diff = abs(target - sum)
                res[0], res[1], res[2] = i, l, h
            if sum < target:
                l += 1
            else:
                h -= 1
        if diff == 0:
            res[0], res[1], res[2] = i, l, h
            break

    print(
        f"The 3 closes indices are {res[0]}:{nums[res[0]]}, {res[1]}:{nums[res[1]]}, {res[2]}:{nums[res[2]]}"
    )
    print(f"\n The closest sum is {target - diff}\n to the target {target}")
    # Return the sum of the three element that is closest to the target
    return target - diff


def three_closest_sum_variation_2(nums: List[int], target: int):
    """
    Given an array , the sum to be extracted (S) we have to find three elements
    whose sum is equal to S. If it is not possible then we find three elements
    whose sum is closest to S.
    Worst case time complexity: Θ(n^2)
    Average case time complexity: Θ(n^2)
    Best case time complexity: Θ(n^2)
    Space complexity: Θ(3*h) (where h is the number of solutions )
    """
    nums.sort()
    temp = 0
    arr = []
    count = 0

    for i in range(len(nums) - 2):
        l, r = i + 1, len(nums) - 1

        while l < r:
            if nums[i] + nums[l] + nums[r] == target:
                print(f"[{nums[i]}, {nums[l]}, {nums[r]}]")
                temp = target
            elif nums[i] + nums[l] + nums[r] < target:
                if temp != target and (nums[i] + nums[l] + nums[r] == temp):
                    arr.append(nums[i])
                    arr.append(nums[l])
                    arr.append(nums[r])
                    temp = nums[i] + nums[l] + nums[r]
                elif temp != target and (
                    abs(nums[i] + nums[l] + nums[r] - target) < abs(temp - target)
                ):
                    arr = [nums[i], nums[l], nums[r]]
                    temp = nums[i] + nums[l] + nums[r]
                l += 1
            else:
                if temp != target and (nums[i] + nums[l] + nums[r] == temp):
                    arr.append(nums[i])
                    arr.append(nums[l])
                    arr.append(nums[r])
                    temp = nums[i] + nums[l] + nums[r]
                elif temp != target and (
                    abs(nums[i] + nums[l] + nums[r] - target) < abs(temp - target)
                ):
                    arr = [nums[i], nums[l], nums[r]]
                    temp = nums[i] + nums[l] + nums[r]
                r -= 1

    for i in range(0, len(arr), 3):
        print(f"[{arr[i]}, {arr[i+1]}, {arr[i+2]}]")
    print(f"The sum is: {temp}")


def find_buildings(heights: List[int]) -> List[int]:
    """
    Find building indices with ocean view to the right
    Iterate from the right
    """
    check = [-1] * len(heights)
    if len(heights) == 1:
        return [0]

    # Traverse the array in reverse
    for i in range(len(heights) - 2, -1, -1):
        if check[i + 1] == -1:
            if heights[i] > heights[i + 1]:
                continue
            else:
                check[i] = i + 1
        else:
            if heights[i] > heights[check[i + 1]]:
                continue
            else:
                check[i] = check[i + 1]

    # print(check)
    # count -1
    ocean_views = []
    for i, val in enumerate(check):
        if val == -1:
            ocean_views.append(i)

    return ocean_views


def findBuildings(heights: List[int]) -> List[int]:
    """
    Iterate from the right, simplify
    Time: O(n)
    space: O(n) worst case [4,3,2,1]
    """
    max_from_right = heights[-1]
    ans = [len(heights) - 1]
    for i in range(len(heights) - 2, -1, -1):
        if heights[i] > max_from_right:
            ans.append(i)
            max_from_right = heights[i]
    return ans[::-1]


def findBuildings(self, heights: List[int]) -> List[int]:
    # Iterate from the left
    # maintain monotonic decreasing stack
    """
    |
    ||
    |||_
    """
    # O(n) O(n)

    n = len(heights)
    stack = []
    for index in range(n):
        while stack and heights[stack[-1]] <= heights[index]:
            stack.pop()
        stack.append(index)
    return stack


def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    cache = {0: -1}
    prefix_sum = 0
    for i in range(len(nums)):
        prefix_sum += nums[i]
        rem = prefix_sum % k
        # print(f'i: {i} rem: {rem}')
        if rem not in cache:
            cache[rem] = i
        elif i - cache[rem] > 1:
            # print(f' i:{i} rem:{rem} cache: {cache}')
            return True
    return False


# three_closest_sum_variation_2([1, 6, 5, 9, 2], 7)
# three_closest_sum_variation_1([-1, 2, 1, -4], 2)
# three_closest_sum_variation_1([0, 0, 0], 1)
rotate_array([1, 2, 3], 4)
rotate_array_right([1, 2, 3], 2)
# print(move_negatives_to_back([-2, 3, 1, -1]))
# print(move_negatives_to_back([2, 0, 1, -1, 0, 1, -1, 0, -1]))
