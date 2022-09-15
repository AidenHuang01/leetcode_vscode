#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
from typing import List
# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # binary search
        if nums[-1] < target:
            return len(nums)
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            elif mid == 0 or nums[mid - 1] < target:
                return mid
            else:
                r = mid - 1
        return r


        
# @lc code=end

