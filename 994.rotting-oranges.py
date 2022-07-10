#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#
from typing import *
# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        def spread(r, c):
            # print(f"spread({r}, {c})")
            if grid[r][c] != 2:
                return
            to_rot = False
            if r+1 < ROWS and grid[r+1][c] == 1:
                grid[r+1][c] += 1
                to_rot = True
            if r-1 >= 0 and grid[r-1][c] == 1:
                grid[r-1][c] += 1
                to_rot = True
            if c+1 < COLS and grid[r][c+1] == 1:
                grid[r][c+1] += 1
                to_rot = True
            if c-1 >= 0 and grid[r][c-1] == 1:
                grid[r][c-1] += 1
                to_rot = True
            grid[r][c] += 1
            
            # print(f"spread({r}, {c}) -> {to_rot}")
            return to_rot
        round = 0
        while True:
            not_finished = False
            active_rot = []
            for i in range(ROWS):
                for j in range(COLS):
                    if grid[i][j] == 2:
                        active_rot.append((i,j))
            # print(f"round {round}, {active_rot}")
            for cor in active_rot:
                not_finished = spread(cor[0], cor[1]) or not_finished
            if not not_finished:
                break
            else:
                round += 1
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return -1
        return round
                    
        

            
        
# @lc code=end

