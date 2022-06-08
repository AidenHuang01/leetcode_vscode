#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#
from typing import List
# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][-1] < target:
                continue
            if matrix[i][0] > target:
                return False
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return True
        return False

# @lc code=end

