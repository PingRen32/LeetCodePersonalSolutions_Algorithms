# Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or
# vertically. You may assume all four edges of the grid are all surrounded by water.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n, res = len(grid[0]), len(grid), 0

        for i in range(m):
            for j in range(n):
                if grid[j][i] == '1':
                    res += 1
                    grid = self.remove(grid, j, i)

        return res

    def remove(self, grid: List[List[str]], j: int, i: int) -> List[List[str]]:
        m, n = len(grid[0]), len(grid)
        grid[j][i] = '0'

        if i > 0 and grid[j][i - 1] == '1':
            grid = self.remove(grid, j, i - 1)
        if i < m - 1 and grid[j][i + 1] == '1':
            grid = self.remove(grid, j, i + 1)
        if j > 0 and grid[j - 1][i] == '1':
            grid = self.remove(grid, j - 1, i)
        if j < n - 1 and grid[j + 1][i] == '1':
            grid = self.remove(grid, j + 1, i)

        return grid

