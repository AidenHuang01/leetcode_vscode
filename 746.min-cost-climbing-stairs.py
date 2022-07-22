#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#
from typing import *
# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mat = [-1 for i in range(len(cost))]
        mat[0] = cost[0]
        mat[1] = cost[1]
        def recur(n):
            if n >= len(mat):
                res = min(recur(n-1), recur(n-2))
                return res
            if mat[n] == -1:
                res = min(recur(n-1), recur(n-2))
                res += cost[n]
                mat[n] = res
                return res
            return mat[n]
        return recur(len(cost))

# @lc code=end

