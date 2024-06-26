---
title: "K Problems"
author: Khoa Le
---

# Kth missing positive number
Given an array of *positive* integers in a strictly increasing order and an integer *k*. Return the K missing number in the array

>input: [2,3,4,7,11] <br>
>k: 5 <br>
>return: 9 <br>
>The missing integers [1,5,6,8,9,10,12,13,...] <br>

```python
def naive_approach(nums: List[int]) -> int:
	"""
	Time: O(n)
	Space: O(n)
	"""	
	cache = set(nums)
	i = 1
	while k > 0:
		if k == 0:
			return i
		if i not in cache:
			k -= 1
		i +=1
	return i - 1
```

### Binary search approach
⭐️  input array is sorted. And the sorted input should ring the bell: "let's try to solve it in a logarithmic time using binary search" <br>

> ⭐️ Given [2,3,4,7,11] length = 5. With an array with no missing number <br>
> [1,2,3,4,5]. These are the numbers of the array if there is no missing number from 1 to n.<br>
> So to find the missing number before nums[i]: nums[i] - i - 1 <br>

![](../resources/missing_positive_number.png)

```python
def find_kth_missing_positive(nums: List[int]) -> int:
	"""
	Time: O(logn)
	Space: O(1)
	"""
	left, right = 0, len(nums) - 1

	while left <= right:
		mid = (right + left) // 2
		# num_missing_positive_before_ith
		if nums[mid] - mid - 1 < k:
			# search the missing positive to the right of mid
			left = mid + 1
		else:
			right = mid - 1 
		
	# once we exit the loop: left = right + 1
	# ⭐️ k-th missing is in between nums[left] nums[right]
	# no. of missing integers before right: nums[right] - right - 1
	return left + k
```
![missing k-th positive](../resources/missing_k-th_positive.png)

# Max Consecutive Ones III
⭐️ Sliding window, keep track of the left and right pointer. <br>
Given a binary array nums and integer k, return the maximum number of consecutive 1s in the array if you can flip k 0s <br>

>Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
>Output: 6
>Explanation: [1,1,1,0,0,1,1,1,1,1,1]
>Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

![max consecutive ones 1](../resources/max_consecutive_ones.png)
![max consecutive ones 2](../resources/max_consecutive_ones2.jpeg)

```python
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
      left = right = 0
      
      for right in range(len(A)):
        # if we encounter a 0 the we decrement K
        if A[right] == 0:
          K -= 1
        # else no impact to K
        
        # if K < 0 then we need to move the left part of the window forward
        # to try and remove the extra 0's
        if K < 0:
          # if the left one was zero then we adjust K
          if A[left] == 0:
            K += 1
          # regardless of whether we had a 1 or a 0 we can move left side by 1
          # if we keep seeing 1's the window still keeps moving as-is
          left += 1
      
      return right - left + 1
```

## Approach 2

Intuition <br>

- Goal: The task is to maximize the length of a subarray consisting of 1's after flipping at most k 0's to 1's. This requires us to find the longest subarray containing at most k 0's.
- Sliding Window Approach: We can think of this problem in terms of a "window" that slides over the array. The idea is to expand the window until we have more thank k 0's and then shrink it from the left until the number of 0's within the window is k or fewer. This way, we maintain a window that has at most k 0's while keeping track of the maximum length of such a window.

```python
def max_ones(nums: List[int], k: int) -> int:
	l = 0
	max_len = 0
	zero = 0

	for r in range(len(nums)):
		if nums[r] == 0:
			zero += 1
		while zero > k:
			# When do we shrink the left pointer. When nums[l] == 0
			# ⭐  If the number of 0's within the window exceeds  𝑘, we move the left pointer to the right to shrink the window until the number of 0's is 𝑘 or fewer.  ️
			if nums[l] == 0:
				zero -= 1
			l += 1
		max_len = max(max_len, r - l + 1)
	
	return max_len

```
Time complexity: <br>
O(n): The algorithm makes a single pass through the array with the right pointer moving from the beginning to the end of the array. The left pointer only moves to the right, and each element is processed at most twice (once by right and once by left). Hence, the overall time complexity is linear, or O(n), where n is the number of elements in the array. <br> 

Space complexity: O(1) <br>

# All K nodes from target node
⭐️ Because the structure of the node doesn't have a parent pointer, so we must figure out how to associate all nodes to the target node. <br>
⭐️ Therefore, we need to connect all node and store them to a data structure <br>

```python
def distance_k(root: TreeNode, target: TreeNode, k: int):
	# connect all nodes
	conn = defaultdict(list) # using default dict so to not throw key error

	def connect(parent, child):
		nonlocal conn

		if parent and child:
			conn[parent.val].append(child.val)
			conn[child.val].append(parent.val)
			# in order traversal to fill the dict
		if child.left:
			connect(child, child.left)
		if child.right:
			connect(child, child.right)
	
	connect(None, root)

	bfs = [target.val]
	seen = set(bfs)

	# We only need to search at most k step from target
	for i range(k):
		new_level = []
		for start_node in bfs:
			for connected_node in conn[start_node.val]:
				# if not seen
				if connected_node not in seen:
					seen.add(connected_node.val)
		# Update the new bfs queue
		bfs = new_level
		seen != set(bfs)
	
	return bfs


```

# Merge K sorted list

## Brute force
⭐️ We want to get tall the node values, sort them, then create a new linked list <br>

```python
def merge_k_brute_force(lists: Optional[ListNode]):
	"""
	Time complexity: O(k*n) + O(nlogn) = O(nlogn) n is the total number of nodes
	Space complexity: O(n)
	"""
	nodes = []
	for list in lists:
		while list:
			nodes.append(list.val)
			list = list.next
	
	head = current = ListNode(-1)
	for i in sorted(nodes):
		current.next = ListNode(i)
		current = current.next
	
	return head.next
```

## Merge 2 list then merge each list
```python
def merge_lists(lists: Optional[ListNode]) -> ListNode:
	def merge_2_lists(list1: ListNode, list2: ListNode) -> ListNode:
		head = current = ListNode(-1)
		while list1 and list2:
			if list1.val <= list2.val:
				current.next = ListNode(list1.val)
				list1 = list1.next
			else:
				current.next = ListNode(list2.val)
				list2 = list2.next
			current = current.next
		# because one of list 1 or list2 will have remaining nodes
		current.next = list1 or list2
		return head.next
	
	if not list:
		return None
	if len(list) == 1:
		return lists[0]
	
	i = 1
	current = lists[0]
	while i < len(lists):
		current = merge_2_lists(current, lists[i])
		i += 1
	return current
```

# Valid Palindrome with K update
Given a string s and an integer k, return true if s is a k-palindrome. <br>
A string is k-palindrome if it can be transformed into a palindrome by removing at most k characters from it. <br>

>Example 1:
>Input: s = "abcdeca", k = 2
>Output: true
>Explanation: Remove 'b' and 'e' characters.

⭐️ With Palindrome we have got to think about 2 pointers approach <b2>
⭐️ It only becomes interesting when s[l] != s[r] <br>
⭐️ Think of each character as a node in a graph. The important decision we have to make is when s[l] != s[r] <br>
 - Take the left character
 - Take the right character

```python
def isValidPalindrome(self, s: str, k: int) -> bool:
	"""
	Time: O(n^2), initialize the visited array. Since there are at most  O(n^2)  pairs and each pair is processed only once, the time complexity for queue operations is  O(n^2) .
	Space: O(n^2)
	"""
	l = 0
	r = len(s) - 1

	queue = deque([(l, r, 0)]) # l, r, k
	visited = [[False for _ in range(len(s))] for _ in range(len(s))]

	while queue:
			l, r, cur_k = queue.popleft()
			if cur_k > k:
				return False

			while s[l] == s[r]:
				l += 1
				r -= 1
				if l >= r:
					return True
			
			if not visited[l+1][r]:
					queue.append((l+1, r, cur_k + 1))
					visited[l+1][r] = True
			
			if not visited[l][r-1]:
					queue.append((l, r-1, cur_k + 1))
					visited[l][r-1] = True

```
