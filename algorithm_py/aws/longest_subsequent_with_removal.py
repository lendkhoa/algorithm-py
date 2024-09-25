"""
HackerLand Sports Club wants to send a team for a relay race. There are n racers in the group indexed from 0 to n. The ith racer has a speed of speed[i] units.
The coach decided to send some contiguous subsegments of racers for the race i.e. racers with index i, i+1, i+2..., such that each racer has the same speed in the group to ensure smooth baton transfer. To achieve the goal, the coach decided to remove some racers from the group such that the number of racers with the same speed in some contiguous segment is maximum.
Given the array, racers, and an integer k, find the maximum possible number of racers in some contiguous segment of racers with the same speed after at most k racers are removed.
Function Description
Complete the function maximumPossibleRacers in the editor.
maximumPossibleRacers has the following parameters:
int[] speed: an array of integers representing the speed of each racer
int k: the maximum number of racers that can be removed
Returns
int: the maximum possible number of racers in some contiguous segment with the same speed after at most k racers are removed
Example 1:
Input:  speed = [1, 4, 4, 2, 2, 4], k = 2
Output: 4 
Explanation:
"""
def longest_subsegment(arr, k):
    n = len(arr)
    max_len = 0

    for target in set(arr):
        left = 0
        count = 0
        curr_len = 0

        for right in range(n):
            if arr[right] == target:
                curr_len += 1
            else:
                count += 1
            while count > k:
                if arr[left] != target:
                    count -= 1
                else:
                    curr_len -= 1
                left += 1
            if count <= k:
                max_len = max(max_len, curr_len)

    return max_len

# Example usage
arr = [1, 4, 4, 2, 2, 4]
k = 2
print(longest_subsegment(arr, k))  # Output: 3

arr = [4, 15, 12, 12, 1]
k = 2
print(longest_subsegment(arr, k))  # Output: 2