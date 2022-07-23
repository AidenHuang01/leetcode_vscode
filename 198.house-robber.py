#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
from typing import *
# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1 for i in range(len(nums))]
        def recurr(s):
            if s >= len(nums):
                return 0
            if memo[s] != -1:
                return memo[s]
            res = max(nums[s] + recurr(s+2), recurr(s+1))
            memo[s] = res
            return res
        return recurr(0)
# @lc code=end

