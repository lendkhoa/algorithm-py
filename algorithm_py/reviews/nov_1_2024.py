from typing import Optional

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def get_height(root: Optional[Node]) -> int:
    print(f'Height of {root.val if root else "None"}')
    if not root:
        return 0
    left = get_height(root.left)
    right = get_height(root.right)
    return max(left, right) + 1

def test_height_1():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    root.right.left = Node(4)
    print(get_height(root))

def test_height_2():
    root = Node(1)
    print(get_height(root))

# Time: O(n^2)
# Space: O(n)
def isBalanced(self, root: Optional[TreeNode]) -> bool:
    # inorder (left root right)
    # preorder(root left right)
    # post order(left right root)
    if not root:
        return True

    left_height = self.get_height(root.left)
    right_height = self.get_height(root.right)
    return abs(left_height-right_height) <= 1

def is_balanced_dfs(root: Optional[Node]) -> bool:
    def dfs(root):
        if not root:
            return [True, 0] # [balanced, height]

        left, right = dfs(root.left), dfs(root.right)
        balanced = left[0] and right[0] and abs(left[1] - right[1])

        return [balanced, 1 + max(left[1], right[1])]

    return dfs(root)[0]
