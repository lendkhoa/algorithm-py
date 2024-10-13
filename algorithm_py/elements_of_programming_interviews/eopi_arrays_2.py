"""
This problem is an example of performing multiple passes on an array
Input: an array of character [a, b, c, c]
2 rules: replace each 'a' by 2 'd'
         remove each entry containing 'b'
remove each 'b' and replaces each 'a' by 2 'd's

We can implement the function without allocating additional space.
- Compute the final length of the array: len + no. of as
- Process the array from left to right
"""

from typing import List

def remove_and_replace(size, s):
    print(f'input {s}')
    write_idx, a_count = 0, 0

    # move write_idx to the size + 1
    for i in range(size):
        if s[i] != 'b':
            s[write_idx] = s[i] # they should be the same
            write_idx += 1
        if s[i] == 'a':
            a_count += 1

    print(f'> write index {write_idx}, acount: {a_count}')
    cur_idx = write_idx - 1
    write_idx += a_count - 1
    final_size = write_idx + 1
    print(f'> write index {write_idx}')

    while cur_idx >= 0:
        if s[cur_idx] == 'a':
            s[write_idx-1:write_idx+1] = 'dd'
            write_idx -= 2
        else:
            s[write_idx] = s[cur_idx]
            write_idx -= 1
        cur_idx -= 1

    print(f'> {write_idx}')
    print(f'> {s}')
    print(f'> {final_size}')

remove_and_replace(3, ['a', 'c', 'a', 'a'])
