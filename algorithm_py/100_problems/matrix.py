from typing import List


def largest_island(grid: List[List[int]]) -> int:
    """
    Return the largest island that can be made if we can transform 1 cell of sea [i][j] = 0
    to land [i][j] = 1.
    """
    n = len(grid)
    island_id = -1
    island_area = {}

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def dfs(grid: List[List[int]], r: int, c: int) -> int:
        nonlocal island_id
        nonlocal directions
        if (0 <= r < len(grid)) and (0 <= c < len(grid[0])) and grid[r][c] == 1:
            # set the island id
            grid[r][c] = island_id

            area = 1

            for r_inc, c_inc in directions:
                new_r = r + r_inc
                new_c = c + c_inc
                area += dfs(grid, new_r, new_c)
            return area
        else:
            return 0

    for m in range(len(grid)):
        for n in range(len(grid[0])):
            if grid[m][n] == 1:
                # kick off dfs
                island_area = dfs(grid, m, n, id)
                island_area[island_id] = island_area
                island_id -= 1

    max_area = 0
    for m in range(len(grid)):
        for n in range(len(grid[0])):
            if not grid[m][n]:
                area = 1
                # check the surrounding cells
                surrounding = set()
                for m_inc, n_inc in directions:
                    new_m = m + m_inc
                    new_n = n + n_inc
                    if (
                        (0 <= new_m < len(grid))
                        and (0 <= new_n < len(grid[0]))
                        and grid[new_m][new_n] != 0
                    ):
                        surrounding.add(grid[new_m][new_n])
                for islandId in surrounding:
                    area += island_area[islandId]
                max_area = max(max_area, area)

    # if the entire grid is 1
    return max_area if max_area > 0 else n**2
