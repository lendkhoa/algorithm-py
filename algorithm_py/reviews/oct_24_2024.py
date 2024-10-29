## Merge
# Time: O(n) n length of shorter array
# Space: O(n)
from typing import List

def merge(a: List[int], b: List[int]):
    merged = []
    inversions = 0
    i, j = 0, 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i])
            i+= 1
        else:
            merged.append(b[j])
            inversions += len(a) - i
            j+=1
    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged, inversions

print(merge([2,4], [1,3]))

# DFS
def dfs(node: Node, graph):
    if not node or node in visited:
        return
    visited.append(node)

    for neighor in graph[node]:
        dfs(neighbor)

def bfs(start):
    queue = deque([start])
    visited = set([start])
    while queue:
        current = queue.pop()
        for neighor in current.neighbor:
            queue.append(neighbor)
            visited.append(neighbor)







