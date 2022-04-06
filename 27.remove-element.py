#
# @lc app=leetcode id=27 lang=python
#
# [27] Remove Element
#

# @lc code=start
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        ptr_left = 0
        ptr_right = len(nums) - 1
        if len(nums) == 1:
            if nums[0] == val:
                nums = []
                return 0
            else:
                return 1
        while ptr_left <= ptr_right:
            if nums[ptr_left] == val:
                nums[ptr_left], nums[ptr_right] = nums[ptr_right], -1
                ptr_left -= 1
                ptr_right -= 1
            ptr_left += 1
        print(nums)
        print(ptr_left)
        return ptr_left

        
# @lc code=end

