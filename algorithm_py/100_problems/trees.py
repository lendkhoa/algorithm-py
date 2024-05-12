from collections import defaultdict, deque
from typing import List, Optional


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
