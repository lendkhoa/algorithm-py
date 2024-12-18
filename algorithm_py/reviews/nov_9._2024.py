"""
Review the min heap and max heap
Time: O(m * logn) m: is the number of time that we will pop from the heap
Space: O(n) n is the length of the queue
"""
import heapq
class KthBiggest:
    def __init__(self, k, nums):
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)
        self.maintain_heap()

    def add(self, num):
        heapq.heappush(self.min_heap, num)
        self.maintain_heap()
    
    def maintain_heap(self):
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

class KthSmallest:
    def __init__(self, k, nums):
        self.k = k
        self.max_heap = nums
        heapq.heapify(self.max_heap)

