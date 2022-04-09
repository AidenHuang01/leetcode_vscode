#
# @lc app=leetcode id=54 lang=python
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        while True:
            slice = matrix[0][:]
            for n in slice:
                res.append(n)
            if len(matrix) <= 1:
                return res
            matrix = self.rotateMatrix(matrix[1:][:])

    def rotateMatrix(self, matrix):
        res = []
        for i in range(len(matrix[0])):
            row = []
            for j in range(len(matrix)):
                row.append(matrix[j][i])
            res.append(row)
        return res[::-1]
# @lc code=end

