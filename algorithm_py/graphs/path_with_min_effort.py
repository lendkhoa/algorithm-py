DESCRIPTION = """
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.
"""
import sys
import heapq
from typing import List

def path_min_effort_dijsktra(heights: List[int]) -> int:
    print(f'{DESCRIPTION}')
    """
    Time: (Rows∗ColsLog(Rows∗Cols))
    |- log(rows * cols): sorting in min heap
    Space: (Rows * cols)
    Finding the shortest path from source (0, 0) -> destination (r-1, c-1)
    F(x) = max(d, ab(h[r][c] - h[neighbor_r][neighbor_c]))
    - dist = [] store the state of the distances
     - mark dist[0][0] = 0
    - minHeap (d, r, c)
    - boundary, distance > dist
    """

    if not heights:
        return -1

    rows, cols = len(heights), len(heights[0])

    # 2D array map Space: O(rows * cols)
    dist = [[sys.maxsize] * cols for _ in range(rows)]
    dist[0][0] = 0
    minHeap = [(0, 0, 0)] # d, r, c
    directions = [left:=(0, -1), (0, 1), (-1, 0), (1, 0)]

    while minHeap:
        distance, row, col = heapq.heappop(minHeap)

        if distance > dist[row][col]:
            continue
        if row == rows - 1 and col == cols - 1:
            return distance
        # go through the neighbor
        for dr, dc in directions:
            nr = row + dr
            nc = col + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                new_distance = max(distance, abs(heights[row][col] - heights[nr][nc]))
                if new_distance < dist[nr][nc]:
                    dist[nr][nc] = new_distance
                    heapq.heappush(minHeap, (new_distance, nr, nc))


    return -1


print(path_min_effort_dijsktra([[1,2,2],[3,8,2],[5,3,5]]))
