from typing import List 
from collections import deque
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

def level_order(root: Node) -> List[int]:
  out = []

  if not root:
    return out

  q = deque()
  q.append(root)
  
  while q:
    level = []
    for _ in range(len(q)):
      node = q.popleft()
      level.append(node.val)
      if node.children:
        q.extend(node.children) 
    out.append(level)
	
  return out

def test():
  root = Node(1)
  root.children = [Node(3), Node(2), Node(4)]
  root.children[0].children = [Node(5), Node(6)]
  print(level_order(root))

test()