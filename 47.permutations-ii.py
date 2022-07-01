#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
from typing import *
# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        track = []
        used = [False] * len(nums)
        nums.sort()
        def backtrack(nums):
            if len(track) == len(nums):
                res.append(track.copy())
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                track.append(nums[i])
                used[i] = True
                backtrack(nums)
                track.pop()
                used[i] = False
        backtrack(nums)
        return res
# @lc code=end

