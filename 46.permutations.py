#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
from typing import *
# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        track = []
        used = [False] * len(nums)
        def backtrack(nums):
            if len(track) == len(nums):
                res.append(track.copy())
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                track.append(nums[i])
                backtrack(nums)
                used[i] = False
                track.pop()
        backtrack(nums)
        return res
# @lc code=end

