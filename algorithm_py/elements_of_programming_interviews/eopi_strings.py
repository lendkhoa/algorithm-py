"""given a string s consists of lowercase latin letters a, b, c. 
 The cost of a string is defined as the sum of the absolute difference of ASCII values of all possib
le pairs of characters present in S. Find the total cost of S. Ex: input: aabbcc, total cost 4 * |97-98| + 4 * |97-99| + 4 * |98-99| = 16
"""

def total_cost(s: str) -> int:
    cost = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] != s[j]:
              print(f'{s[i]} - {s[j]}')
              cost += abs(ord(s[i]) - ord(s[j]))
    return cost

def total_cost_test():
  assert total_cost("aaaaa") == 0
  assert total_cost("aabbcc") == 16
  assert total_cost("abcde") == 20

# total_cost_test()
print(total_cost('askfjk'))