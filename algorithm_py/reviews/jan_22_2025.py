from typing import Optional

class Node:
    def __init__(self, val=0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}

        # Deep clone the completely new graph
        # Time: O(N) to go through all the nodes
        def dfs(node: Optional['Node']):
            # return the cloned node
            nonlocal old_to_new # hashmap to keep track of old to new node

            if not node:
                return;
            if node in old_to_new:
                return old_to_new[node] # return the cloned

            copy = Node(node.val)
            old_to_new[node] = copy

            for n in node.neighbors:
                copy.neighbors.append(dfs(n))

            return copy if node else None

        return dfs(node)

    def cloneGraphBFS(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_to_new = {}
        queue = collections.defaultlist([node])

        while queue:
            cur = queue.popleft()
            for n in cur.neighbors:
                if n not in old_to_new:
                    old_to_new[n] = Node(n.val)
                    queue.append(n)
                old_to_new[cur].neighbors.append(old_to_new[n])

        return old_to_new[node]



def test_clone_1():
    a = Node(1, None)
    solution = Solution()
    a_cloned = solution.cloneGraph(a)

    print(f'Old id: {id(a)} vs {id(a_cloned)}')


def run_tests():
    test_clone_1()


run_tests()
