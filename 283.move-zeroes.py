#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
from typing import List
# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, 1
        while l < len(nums) and r < len(nums):
            if nums[l] == 0:
                while r < len(nums)-1 and nums[r] == 0:
                    r += 1
                nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r += 1
# @lc code=end

