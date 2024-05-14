# Reverse the number
![Image Description](../resources/traverse_integer_right_left.jpeg)
Traversing the array from RIGHT -> LEFT
```python
# Time complexity: O(n) n is the number of digits in x
def reverse(x: int) -> int:
  res = 0
  rem = abs(x)
  # Base 10
  while rem:
    res = res * 10 + rem % 10
    rem //= 10
  return -res if x < 0 else res
```

# Re-create the number from left to right from String ↪️

When we need to iterate the string to create a number from characters

```python
def create_number(s: str) -> int:
  n = 0
  for i in range(len(s)):
    n = 10 * n + int(s[i])
    print(f'n: {n}')
  return n
```

# Re-create the number from right to left from String ↩️
![String input - traverse from right to create integer](../resources/str_input_traverse_right_left_create_int.jpeg)
```python
def parse_string_from_right(s: str) -> int:
    n = 0
    i = 0
    operand = 0
    for i in range(len(s) - 1, -1, -1):
      print(f'n: {n} | op: {operand} | {s[i]}')
      operand += 10**n * int(s[i])
      n += 1
      print(f'> n: {n} | op: {operand}')
    return operand
```

# Check if a decimal number is palindromic
- If the number is negative then it is not palindromic
- Need to check the most significant bit vs the least significant big, iteratively
- LSB: n mod 10
- MSB: n / 10** (n-1)
```python
def is_palindrome_number(x: int) -> bool:
  if x <= 0:
    return x == 0
  num_digits = math.floor(math.log10(x)) + 1
  msd_mask = 10 ** (num_digits - 1)
  for i in range(num_digits // 2):
    if x // msd_mask != x % 10:
      return False
    else:
      x %= msd-mask # Renove the nost significant digit of x 
      x //= 10 # Renove the least significant digix of x. 
      msd-mask //= 100
```

# Find intersected intervals
You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3]

⭐️ How do we determine if 2 intervals intersect?
```python
# [s1, e1] vs [s2, e2]
def intersected(listA: List[int], listB: List[int]) -> bool:
  # There are too many check for a intersected
  # Instead we check for the two list not to be intersected
  if listA[1] < listB[0] or listB[1] < listA[0]:
    return False
  return True
```

⭐️ How do we alternatively process each element of the element?
Thinking about binary search. Using 2 pointers.
![intersected intervals](../resources/intersected_intervals.jpeg)
```python
def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
  result = []
  i, j = 0, 0

  while i < len(firstList) and j < len(secondList):
      list_i = firstList[i]
      list_j = secondList[j]
      if self.intersect(list_i, list_j):
          result.append([max(list_i[0], list_j[0]), min(list_i[1], list_j[1])])
      
      # move pointers
      # ⭐️ if the end list 1 < end of list 2 and we already process the intersected
      # then we should increment i
      if list_i[1] < list_j[1]:
          i += 1
      else:
          j += 1
      
  return result
```

# Find and return the intersect Rectangle
Given the Rectangle can be create with this class
```python
Rectangle(x, y, width, height)
```
There is a list of rectangles, determine if they intersect and return the intersected rectangle
![intersect_rectangles](../resources/intersected_rectangles.jpeg)
```python
def intersect_rectangles(rectA, rectB):
  def is_intersected(rectA, rectB):
      return (rectA.x <= rectB.x + rectB.w and rectB.x <= rectA.x + rectA.w and
                  rectA.y <= rectB.y + rectB.h and rectB.y <= rectA.y + rectA.h)

  if not is_intersected(rectA, rectB):
    # return an empty rectangle
    return Rectangle(0,0, -1, -1)

  return Rectangle(max(rectA.x, reactB.x),
                   max(rectA.y, rectB.y),
                   min(x1+w1, x2+w2) - max(x1, x2), 
                   min(y1+h1, y2+h2) - max(y1, y2))
```