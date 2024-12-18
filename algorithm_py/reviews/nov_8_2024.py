"""
Find the K largest element in the stream
"""
from typing import List
import heapq

# Space: O(k) for the heap
# Time: O(m*logk)
class KthLargest:
  def __init__(self, k, nums):
    self.k = k
    self.min_heap = nums
    heapq.heapify(self.min_heap)
    self.maintain_heap()

  def maintain_heap(self):
    while len(self.min_heap) > self.k:
      heapq.heappop(self.min_heap)
  
  def add(self, val):
    heapq.heappush(self.min_heap, val)
    self.maintain_heap()
    return self.min_heap[0]

# convert this code to find the Kth smallest

import heapq
class Solution:
	def lastStoneWeight(self, stones: List[int]) -> int:
		# create max heap
		max_heap = [-stone for stone in stones]
		heapq.heapify(max_heap)

		while len(max_heap) >= 2:
				first = -heapq.heappop(max_heap)
				second = -heapq.heappop(max_heap)
				if first == second:
						continue
				elif first < second:
						heapq.heappush(max_heap, -(second-first))
				else:
						heapq.heappush(max_heap, -(first-second))
		
		return -max_heap[0] if max_heap else 0

