"""
Word search
2-D grid of characters. Return True if the word is present
in the grid.
Example:
word = "ABCCED"
grid = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]
Output: True
"""
from typing import List
# Time: O(m * 4^n)
def word_search(board: List[List[str]], word: str) -> bool:
    ROWS, COLS = len(board), len(board[0])
    path = set()

    def dfs(cell, i):
        # exit condition 
        if i == len(word):
            return True
        # exit condition 2; out of bound
        r, c = cell
        if r < 0 or c < 0 or r >= ROWS or c >= COLS or cell in path or board[r][c] != word[i]:
            return False
        
        path.add(cell)
        left, right, top, down = (0, -1), (0, 1), (-1, 0), (1, 0)
        res = dfs(left, i+1) or dfs(right, i+1) or dfs(top, i+1) or dfs(down, i+1)
        path.remove(cell)
        
        return res
    
    for r in range(ROWS):
        for c in range(COLS):
            if dfs((r, c), 0):
                return True
    
    return False