#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        mat = [-1 for i in range(n+1)]
        mat[0] = 1
        mat[1] = 1
        def recur(n):
            # print(f"mat={mat}, n={n}")
            if mat[n] == -1:
                res = recur(n-1) + recur(n-2)
                mat[n] = res
                return res
            return mat[n]
        return recur(n)
# @lc code=end

