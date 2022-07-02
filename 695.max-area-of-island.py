#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#
from typing import *
# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        res = 0
        visited = [[False for c in range(COL)] for r in range(ROW)]
        def dfs(r, c, grid) -> int:
            if min(r,c) < 0 or r >= ROW or c >= COL:
                return 0
            if visited[r][c]:
                return 0
            if grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            area = 1
            area += dfs(r+1, c, grid) +\
                    dfs(r-1, c, grid) +\
                    dfs(r, c+1, grid) +\
                    dfs(r, c-1, grid)
            return area
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    area = dfs(r, c, grid)
                    res = max(area, res)
        return res

# @lc code=end

