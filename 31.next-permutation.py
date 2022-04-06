#
# @lc app=leetcode id=31 lang=python
#
# [31] Next Permutation
#

# @lc code=start


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-1
        while i > 0:
            if nums[i-1] < nums[i]:
                self.reverse(nums, i, len(nums)-1)
                for j in range(i, len(nums)):
                    if nums[i-1] < nums[j]:
                        self.swap(nums, i-1, j)
                        return
            i -= 1
        self.reverse(nums, 0, len(nums)-1)
        return

    def swap(self, nums, x, y):
        nums[x], nums[y] = nums[y], nums[x]
    
    def reverse(self, nums, beg, end):
        while beg < end:
            self.swap(nums, beg, end)
            beg += 1
            end -= 1
                
# @lc code=end

