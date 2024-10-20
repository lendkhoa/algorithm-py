"""
Given a string , find largest substring not having any prohibited strings .Only return maximum length of possible substring .

Eg - Input string - "FastDeliveryOkayProduct" - prohibited strings - ["yo","eli","eryokay"]
Largest possible string - "kayProduct" - Output Answer-> 11
"""
from typing import List, Optional
# Time: O(2*n * m)
def inefficient(input_str, prohibited: List[str]):
    # 2 loops start - end
    max_length = 0
    win_start = 0
    input_str = input_str.lower()

    for win_end in range(len(input_str)):
        print(f'{win_start} : {win_end}')
        for prohibited_str in prohibited:
            print(f'Checking {input_str[win_start:win_end+1]}')
            if input_str[win_start:win_end+1].find(prohibited_str) != -1:
                # move the window
                win_start = win_end + 1
                break
            else:
                max_length = max(max_length, win_end-win_start + 1)
    return input_str[win_start: win_end+1], max_length

# print(inefficient('FastDeliveryOkayProduct', ['yo', 'eli', 'eryokay']))

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

    def content(self):
        return list(self.children.keys())

def build_trie(prohibited: List[str]):
    root = TrieNode()
    for word in prohibited:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    return root

def traverse_trie(root: Optional[TrieNode]):
    if not root:
        return
    print(root.content())

    for child_key in root.children:
        traverse_trie(root.children[child_key])

root = build_trie(['hi', 'my', 'name', 'is'])
# traverse_trie(root)

def max_length_of_substring(input_str, prohibited):
    root = build_trie(prohibited)
    max_length = 0
    max_substring = ""
    window_start = 0
    node = root
    input_str = input_str.lower()

    for window_end in range(len(input_str)):
        char = input_str[window_end]
        if char in node.children:
            node = node.children[char]
            if node.is_end_of_word:
                # Move window forward
                window_start = window_end - len(max(prohibited, key=len)) + 1
                node = root
        else:
            node = root
            window_start = window_end + 1

        if window_end - window_start + 1 > max_length:
            max_length = window_end - window_start + 1
            max_substring = input_str[window_start:window_end + 1]

    return max_substring, max_length



print(max_length_of_substring('FastDeliveryOkayProduct', ['yo', 'eli', 'eryokay']))





