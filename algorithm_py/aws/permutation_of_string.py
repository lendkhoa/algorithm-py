"""
Given two strings s1 and s2, return true if s2 contains a 
permutation
 of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

"""
def checkInclusionNaive(s1: str, s2: str) -> bool:
    # Time: O(nlogn)
    # Space: O(m) m in length of s1
    # s1 is the shorter string
    s1 = ''.join(sorted(s1))
    # we only need to interate through index i-th at len of s1
    for i in range(len(s2) - len(s1) + 1):
        # compare the sorted string of s2 slice
        if s1 == ''.join(sorted(s2[i: i+len(s1)])):
            return True
    return False

