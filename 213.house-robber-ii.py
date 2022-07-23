#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#
from typing import *
# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        loop1 = nums[:-1]
        loop2 = nums[1:]
        def recurr(s, loop, memo):
            if s >= len(memo):
                return 0
            if memo[s] != -1:
                return memo[s]
            res = max(loop[s]+recurr(s+2, loop, memo), recurr(s+1, loop, memo))
            memo[s] = res
            return res
        memo1 = [-1 for i in range(len(loop1))]
        memo2 = [-1 for i in range(len(loop2))]
        res1 = recurr(0, loop1, memo1)
        res2 = recurr(0, loop2, memo2)
        return max(res1, res2)        
# @lc code=end

