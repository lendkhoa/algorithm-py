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