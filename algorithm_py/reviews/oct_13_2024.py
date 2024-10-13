"""
Bellman Ford. Detect negative weighted cycle in directed graph
Cheapest price with k stops
- Find the shortest path from source n to all source.
"""
# Time: O(k * flights)
# Space: O(n)
def cheapestPriceWithKStops(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    INF = sys.maxsize
    previous = [INF] * n
    current = [INF] * n
    previous[src] = 0

    for i in range(1, k+1): # want to check up until k
        for flight in flights:
            prev_flight, current_flight, cost = flight
            if previous[prev_flight] < INF: # we were there before
                current[currrent_flight] = min(current[current_flight], previous[prev_flight] + cost)
        previous = current[:]

    return -1 if current[dst] == INF else current[dst]

