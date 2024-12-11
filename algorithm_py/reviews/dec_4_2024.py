"""Least interval
"""
# N is the number of space between the duplicate task
# We will add idle time in between the most frequent tasks. n=2 AAABB - AB_AB_A
# when we think about freq -> heap (maxHeap) -> max heap helps us to always find the most frequent task

from collections import Counter, deque
import heapq

def leastInterval(tasks, n):
    counter = Counter(tasks)
    # Find the most frequent task
    max_heap = [-cnt for cnt in counter.values()]
    heapq.heapify(max_heap)

    # we want to be able to keep track of the task_idx and when we can append the
    # task back to the heap
    task_idx = 0
    time_idx = 1
    q = deque() # [-cnt, idle_time]
    while max_heap or q:
        time += 1
        if not max_heap:
            time = q[task_idx][time_idx] # idle time
        else:
            cnt = 1 + heapq.heappop(max_heap) # negative, add 1 to decrease the count
            if cnt != 0: # we still have instance of this task
                q.append([cnt, time + n])

        if q and q[task_idx][time_idx] == time:
            heapq.heappush(max_heap, q.popleft()[task_idx])
    return time