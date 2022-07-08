#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#
from typing import *
# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != "O":
                return
            board[r][c] = "T"
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        # mark alive pieces as "T"
        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or r == ROWS-1 or c == 0 or c == COLS-1) and board[r][c] == "O":
                    dfs(r, c)
        # eat all dead pieces
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        # restore all alive pieces from "T" to "O"
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
        
        
# @lc code=end

