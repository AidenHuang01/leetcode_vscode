#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
from typing import *
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 1, 1
        current = nums[0]
        while fast < len(nums):
            if nums[fast] != current:
                nums[slow] = nums[fast]
                current = nums[fast]
                slow += 1
                fast += 1
            else:
                fast += 1
        return slow

# @lc code=end

