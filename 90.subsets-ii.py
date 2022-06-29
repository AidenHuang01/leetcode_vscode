#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#
from typing import *
# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        track = []
        nums.sort()
        def backtrack(nums, start):

            res.append(track.copy())

            for i in range(start, len(nums)):
                
                if i > start and nums[i] == nums[i-1]:
                    continue

                track.append(nums[i])
                backtrack(nums, i + 1)
                track.pop()
        
        backtrack(nums, 0)
        return res
# @lc code=end

