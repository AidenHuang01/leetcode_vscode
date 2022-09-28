#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#
from typing import *
# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])
        # Frist step: reverse the rows
        matrix.reverse()

        # Second step: swap diagno elements
        for r in range(ROWS - 1):
            for c in range(r+1, COLS):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        
        
# @lc code=end

