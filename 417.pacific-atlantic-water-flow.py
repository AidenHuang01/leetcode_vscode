#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#
from typing import *
# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW = len(heights)
        COL = len(heights[0])
        pac = set()
        alt = set()

        def dfs(r, c, visited, prev):
            if (r,c) in visited or min(r,c) < 0 or r >= ROW or c >= COL or heights[r][c] < prev:
                return
            visited.add((r,c))
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])

        for c in range(COL):
            dfs(0, c, pac, heights[0][c])
            dfs(ROW-1, c, alt, heights[ROW-1][c])
        
        for r in range(ROW):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COL-1, alt, heights[r][COL-1])
        
        res = []
        for c in range(COL):
            for r in range(ROW):
                if (r, c) in pac and (r, c) in alt:
                    res.append((r, c))
        return res

# @lc code=end

