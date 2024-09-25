# Greedy
import heapq


def change_making (cents) :
  COINS = [100, 50, 25, 10, 5, 1]
  num_coins = 0
  for coin in COINS:
    num_coins += cents // coin
  cents %= coin 
  
  return num_coins

# Krushkal's algorithm
class UnionFind:
  def __init__(self, size):
    self.root = [i for i in range(size)]
    self.rank = [1] * size
  def find(self, x):
    if x == self.root[x]:
      return x
    self.root[x] = self.find(self.root[x]) # path compression
    return self.root[x]
  
  def union(self, x, y):
    rootX = self.find(x)
    rootY = self.find(y)
    if rootX != rootY:
      if self.rank[rootX] > self.rank[rootY]:
        self.root[rootY] = rootX
      elif self.rank[rootX] < self.rank[rootY]:
        self.root[rootX] = rootY
      else:
        self.root[rootY] = rootX
        self.rank[rootX] += 1

# O(ElogE). Here, E represents the number of edges.
def min_cost_to_connect_points(points):
  n = len(points)
  edges = []
  # build all the edges
  for curr_node in range(n):
    for next_node in range(curr_node + 1, n):
      weight = abs(points[curr_node][0] - points[next_node][0]) + abs(points[curr_node][1] - points[next_node][1])
      edges.append((weight, curr_node, next_node))
  
  # sort the edges in ascending order
  edges.sort()

  uf = UnionFind(n)
  mst_cost = 0
  for weight, u, v in edges:
    if uf.find(u) != uf.find(v):
      uf.union(u, v)
      mst_cost += weight

  return mst_cost  

class Edge:
    def __init__(self, point1, point2, cost):
        self.point1 = point1
        self.point2 = point2
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

def min_cost_to_connect_points_prim(points):
  n = len(points)
  if not points or n == 0:
    return 0
  
  pq = []
  visited = [False] * n
  result = 0
  
  count = n - 1
  # Add all edges from points[0] vertex
  x1, y1 = points[0]
  for j in range(1, n):
    x2, y2 = points[j]
    cost = abs(x1 - x2) + abs(y1 - y2)
    pq.append(Edge(0, j, cost))
  
  # convert pq to heap
  heapq.heapify(pq)
  visited[0] = True

  while pq and count > 0:
    edge = heapq.heappop(pq)
    point1 = edge.point1
    point2 = edge.point2
    cost = edge.cost
    
    if not visited[point2]:
      result += cost
      visited[point2] = True
      count -= 1

      # Add all vertexes from points
      for k in range(n):
        if not visited[k]:
          cost = abs(points[point2][0] - points[k][0]) + abs(points[point2][1] - points[k][1])
          heapq.heappush(pq, Edge(point2, k, cost))
  
  return result 