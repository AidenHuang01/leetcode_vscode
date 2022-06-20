#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#
from typing import List
# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            print(f"l={l}, r={r}, m={m}  l={nums[l]}, r={nums[r]}, mid={nums[m]}")
            # on the left
            if nums[m] >= nums[0]:
                l = m + 1
            else:
                r = m - 1
        return nums[l]
# @lc code=end

