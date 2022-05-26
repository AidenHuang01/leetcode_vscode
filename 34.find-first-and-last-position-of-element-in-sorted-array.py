#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
from typing import List
# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = -1
        end = -1
        for i in range(len(nums)):
            if nums[i] == target:
                start = i
                end = i
                while end+1 < len(nums) and nums[end+1] == target:
                    end += 1
                return [start, end]
        return [-1, -1]
# @lc code=end

