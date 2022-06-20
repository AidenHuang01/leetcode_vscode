#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#
from typing import List
# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Floyd's Algorithm
        f = 0
        s = 0
        while True:
            f = nums[f]
            f = nums[f]
            s = nums[s]
            if f == s:
                break
        s2 = 0
        while True:
            s = nums[s]
            s2 = nums[s2]
            if s == s2:
                return s
# @lc code=end

