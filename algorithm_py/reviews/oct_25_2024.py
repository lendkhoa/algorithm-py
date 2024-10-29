"""
Reverse a linkedlist
"""
from dataclasses import dataclass

@dataclass
class Node:
    val: int
    nxt: 'Node' = None

def reverseLinkedList(node: Node):
    prev = None
    current = node
    while current:
        nxt = current.nxt
        current.nxt = prev
        prev = current
        current = nxt
    return prev

def test_reverse():
    one = Node(1, None)
    two = Node(2, None)
    one.nxt = two

    reverse = reverseLinkedList(one)
    while reverse:
        print(reverse.val)
        reverse = reverse.nxt


"""
Adding 2 linked list
1->2->3
   3->4
"""

def add_lists(l1, l2):
    carry = 0
    anchor = Node()
    current = anchor

    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        s_v = v1 + v2 + carry

        # update the carry 29+9 = 8
        carry = s_v // 10
        s_v = s_v % 10
        current.nxt = Node(s_v)
        current = current.next
        l1 = l1.nxt if l1 else None
        l2 = l2.nxt if l2 else None
    return dummy.nxt

"""
Longest repeating substring with K replacement
XYYX K=2
XXXX or YYYY = 4
⭐️  we want to replace the least frequent character
    we want the longest string to match the most frequent character
    len(w) - count[most_frequent] <= K
⭐️   The original order is important so we can't change it, process it as we go -> sliding window
     Most frequent -> hashmap
"""

def longestRepeating(s: str, k: int):
    left = 0
    maxF = 0
    count = {}

    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1
        maxF = max(maxF, count[s[right]])
        # when do we shrink the window
        if (right - left + 1) - maxF > k:
            print(f'left: {left} | right: {right} => {count}')
            count[s[left]] -= 1
            left += 1
    return right - left + 1

def test_longest_repeating_with_k():
    print(longestRepeating('xyyxbbb', 2))

test_longest_repeating_with_k()





















