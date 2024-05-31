from collections import defaultdict, deque
from typing import List, Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:  # type: ignore
    """
    Time complexity: O(N)
    Space: O(N)
    """
    if not root:
        return []

    columns = defaultdict(list)

    q = deque([(root, 0)])
    while q:
        node, x = q.popleft()
        columns[x].append(node.val)

        if node.left:
            q.append((node.left, x - 1))
        if node.right:
            q.append((node.right, x + 1))

    return [columns[x] for x in range(min(columns), max(columns) + 1)]


def verticalOrder_dfs(self, root: TreeNode) -> List[List[int]]:  # type: ignore
    """
    Time complexity: O(W⋅HlogH)) where W is the width of the binary tree (i.e. the number of columns in the result)
    and H is the height of the tree.
    Space complexity: O(N)
    """
    if root is None:
        return []

    columnTable = defaultdict(list)
    min_column = max_column = 0

    def DFS(node, row, column):
        if node is not None:
            nonlocal min_column, max_column
            columnTable[column].append((row, node.val))
            min_column = min(min_column, column)
            max_column = max(max_column, column)

            # preorder DFS
            DFS(node.left, row + 1, column - 1)
            DFS(node.right, row + 1, column + 1)

    DFS(root, 0, 0)

    # order by column and sort by row
    ret = []
    # O(KlogK) where K is the length of the input.
    for col in range(min_column, max_column + 1):
        columnTable[col].sort(key=lambda x: x[0])
        colVals = [val for row, val in columnTable[col]]
        ret.append(colVals)

    return ret


"""
ALL NODE DISTANCE K in BINARY TREE
"""


def distanceK(root: TreeNode, target: TreeNode, k: int) -> List[int]:
    conn = defaultdict(list)

    def connect(parent: TreeNode, child: TreeNode):
        if parent and child:
            # building an undirected graph
            conn[parent.val].append(child.val)
            conn[child.val].append(parent.val)
        # in-order traversal
        if child.left:
            connect(child, child.left)
        if child.right:
            connect(child, child.right)

    connect(None, root)
    print(f"Connect: {conn}")

    bfs = [target.val]
    seen = set(bfs)

    # we only need to run the search for k step
    for i in range(k):
        new_level = []
        for start_node in bfs:
            for connected_node in conn[start_node]:
                if connected_node not in seen:
                    new_level.append(connected_node)
        bfs = new_level
        # union, add all val in bfs to seen
        seen |= set(bfs)
        print(f" bfs: {bfs} | {seen}")

    return bfs


def test_distanceK():
    # create tree (directed graph)
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)

    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)

    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    distanceK(root, root.left, 2)


test_distanceK()
