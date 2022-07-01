#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#
from typing import *
# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if nums[0] >= 0:
            res = [x**2 for x in nums]
            return res
        if nums[-1] <= 0:
            nums.reverse()
            res = [x**2 for x in nums]
            return res
        mid = -1
        for i in range(len(nums)):
            if i > 0 and nums[i-1] < 0 and nums[i] >= 0:
                mid = i
        l, r = mid-1, mid
        res = []
        while l >= 0 and r < len(nums):
            if abs(nums[l]) < abs(nums[r]):
                res.append(nums[l]**2)
                l -= 1
            else:
                res.append(nums[r]**2)
                r += 1
        if l >= 0:
            for i in range(l, -1, -1):
                res.append(nums[i]**2)
        if r < len(nums):
            for i in range(r, len(nums)):
                res.append(nums[i]**2)
        return res
            
# @lc code=end

