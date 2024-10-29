"""
Notes:
Special String: A string is special if there are no two adjacent characters that are the same.
Lexicographical Order: This is a generalization of the way words are alphabetically ordered in dictionaries. For example, "abc" is lexicographically smaller than "abd" because 'c' comes before 'd' in the alphabet.
A string a is lexicographically smaller than a string b if and only if one of the following holds:


a is a prefix of b, but is not equal to b. For example, "abc" is smaller than "abcd".
In the first position where a and b differ, the character in a comes before the character in b in the alphabet. For example, "abc" is smaller than "abd" because 'c' comes before 'd'.
Important Considerations:
If the character is 'z', it is the last character in the alphabet and cannot be increased further. The string should not wrap around to 'a' after 'z'.
The output string must not have any adjacent characters that are the same.
"""

def getSpecialString(n: int, s: str) -> str:
    if len(s) == 1 and ord(s[0]) - ord('a') == 26:
        return s
    if len(s) == 1:
        index = ord(s[0]) + 1
        return chr(ord(s[0]) + 1)

    j = 0
    for i in range(1, n):
        if ord(s[i]) - ord(s[i-1]) == 0:
            j = i
    print(s)
    print(f'Need update {j}')

# print(getSpecialString(1, 'a'))
# print(getSpecialString(4, 'abbd'))
# getSpecialString(4, 'abbd')

def next_lexicographic(s):
    s = list(s)
    n = len(s)
    i = n - 2

    # Find the first character from the right that is smaller
    while i >= 0 and s[i] >= s[i + 1]:
        i -= 1
    if i == -1:  # No next lexicographic string
        return None
    s[i] = chr(ord(s[i]) + 1)
    # Set all characters to its right to 'a'
    for j in range(i + 1, n):
        s[j] = 'a'
    return ''.join(s)

# Test
print(next_lexicographic('abbd'))  # abca
print(next_lexicographic('abbb'))
print(next_lexicographic('zzab'))
