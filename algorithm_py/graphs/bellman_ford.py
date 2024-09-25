import sys
from typing import List

def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
	if src == dst:
			return 0
	
	INF = sys.maxsize
	previous = [INF] * n
	current = [INF] * n
	previous[src] = 0
	
	for i in range(1, k + 2):
		print(f'Previous {previous}')
		print(f'Current {current}')
		current[src] = 0
		for u, v, c in flights:
			print(f' u: {u} v: {v} c: {c}')
			if previous[u] < INF:
				print(f'  previous[u] {previous[u]}')
				print(f'  compare current[v] {current[v]} vs {previous[u]} + {c}')
				current[v] = min(current[v], previous[u] + c)
				print(f'    current[v] {current[v]}')
						
		previous = current.copy()
			
	return -1 if current[dst] == INF else current[dst]

flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
print(f"Cheapest price: {findCheapestPrice(len(flights), flights, 0, 2, 2)}")