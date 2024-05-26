# Sum root to leaf
You are given the root of a binary tree containing digits from 0 to 9 only.
Each root-to-leaf path in the tree represents a number.
For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.

⭐️ We need to keep track of the previous integer value

![sum root to leaf](../resources/root_to_leaf.jpg)
```python
def sum_root_to_leaf(root: Optional[TreeNode]) -> int:
	"""
	Return the sum of the integer value from root to leaf
	Assumption: root's val is not 0. No negative
	Time complexity: O(n)
	Space complexity: O(h). H is the height of the tree
	"""

	# 
	def dfs(node: Optional[TreeNode], n: int) -> int:
		if not node:
			return 0
		
		n = 10 * n + int(node.val)

		if node.left is None and node.right is None:
			return n

		return dfs(node.left, n) + dfs(node.right, n)
	
	return dfs(root)
```

# Flatten binary tree to linked list
Given the root of a binary tree, flatten the tree into a "linked list":
The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
⭐️ Following the pre order traversal (root - left - right)
⭐️ Each root has no left child, and the right child is linked to the lowest left child

![flatten binary tree](../resources/flatten_bt.jpg)

```python
# Assume the TreeNode
"""
class TreeNode:
	val: int
	left: TreeNode
	right: TreeNode
"""
def flatten(root: Optional[TreeNode]) -> None:
	
	def pre_order(node: Optional[TreeNode]) -> TreeNode:
		"""
		Traverse the tree in pre order order
		"""
		if not node:
			return None
		if node.left is None and node.right is None:
			return node
		left = pre_order(node.left)
		if left:
			# Update the current node's right child to be the left one
			node.right = left
			current = left
			prev = None
			while current:
				current = prev
				current = current.right
		prev.right = right
		node.left = None
		return node
	
	return pre_order(root)
```