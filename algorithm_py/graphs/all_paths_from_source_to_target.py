from collections import deque
from typing import List

def bfs(graph: List[List[int]]) -> List[List[int]]:
  """Find all path from source to destination
  Input: graph = [[1,2],[3],[3],[]]
  Output: [[0,1,3],[0,2,3]]
  Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

  For a graph with V vertices, there could be at most 2^(v-1) -1 possible paths to go from the starting vertex to the target vertex. We need 
  O(V) time to build each such path.

  Args:
      graph (List[List[int]]): _description_

  Returns:
      List[List[int]]: _description_
  """

  paths = []
  
  if not graph or len(graph) == 0:
    return []
  
  queue = deque()
  path = [0]
  queue.append(path)

  while queue:
    current_path = queue.popleft()
    node = current_path[-1]
    for next_node in graph[node]:
      temp_path = current_path.copy()
      temp_path.append(next_node)
      if next_node == len(graph) - 1:
        paths.append(temp_path)
      else:
        queue.append(temp_path)
  
  return paths

def bfs_a_test() -> None:
  graph = [[1, 2],[3],[],[]]
  # expect [0, 1, 3]
  print(bfs(graph))

bfs_a_test()


def dfs(graph: List[List[int]]) -> List[List[int]]:
  """Find all path from source to destination
  Input: graph = [[1,2],[3],[3],[]]
  Output: [[0,1,3],[0,2,3]]
  Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

  For a graph with V vertices, there could be at most 2^(v-1) -1 possible paths to go from the starting vertex to the target vertex. We need
  O(V) time to build each such path.

  Args:
      graph (List[List[int]]): _description_

  Returns:
      List[List[int]]: _description_
  """

  paths = []

  if not graph or len(graph) == 0:
    return []
  
  def helper(node: int, path: List[int]) -> List[List[int]]:
    if node == len(graph) - 1:
      paths.append(path.copy())
      return
    
    for next_node in graph[node]:
      path.append(next_node)
      helper(next_node, path)
      path.pop()
    
  helper(0, [0])
  
  return paths 

def dfs_a_test() -> None:
  graph = [[1, 2],[3],[],[]]
  # expect [0, 1, 3]
  print(dfs(graph))

dfs_a_test()