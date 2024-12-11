"""Task scheduler
"""
from typing import List
from collections import Counter, deque
import heapq

def leastInterval(tasks: List[str], n: int) -> int:
    count = Counter(tasks)
    maxHeap = [-cnt for cnt in count.values()]

    heapq.heapify(maxHeap)

    time = 0
    TASK_IDX=0
    TIME_IDX=1
    q = deque() # pairs of [-cnt, idleTime]
    while maxHeap or q:
        print(f'{maxHeap} --- {q}')
        time += 1
        
        if not maxHeap:
            time = q[TASK_IDX][TIME_IDX]
            print(f'Not maxheap {time}')
        else:
            cnt = 1 + heapq.heappop(maxHeap)
            print(f'cnt {cnt} {q}')
            if cnt:
                q.append([cnt, time+n])
                print(f'>> {q}')
        if q and q[TASK_IDX][TIME_IDX] == time:
            heapq.heappush(maxHeap, q.popleft()[TASK_IDX])
    return time

leastInterval(["A", "A", "A", "B", "B", "B"], 2)