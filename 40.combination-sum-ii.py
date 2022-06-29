#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
from typing import *

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        track = []
        self.track_sum = 0
        self.target = target
        candidates.sort()
        def backtrack(nums,start):
            if self.track_sum == self.target:
                res.append(track.copy())
                return
            if self.track_sum > self.target:
                return
            for i  in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                track.append(nums[i])
                self.track_sum += nums[i]
                backtrack(nums, i + 1)
                track.pop()
                self.track_sum -= nums[i]
        backtrack(candidates, 0)
        return res
# @lc code=end

