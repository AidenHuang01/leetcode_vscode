#
# @lc app=leetcode id=215 lang=python
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
from heapq import heapify, heappop


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def quickSelect(nums, l, r):
            if l == r:
                return nums[l]
            pivot = nums[r]
            ptr = l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[ptr], nums[i] = nums[i], nums[ptr]
                    ptr += 1
            nums[ptr], nums[r] = nums[r], nums[ptr]

            if ptr > len(nums) - k:
                return quickSelect(nums, l, ptr - 1)
            elif ptr < len(nums) - k:
                return quickSelect(nums, ptr + 1, r)
            else:
                return nums[ptr]
        return quickSelect(nums, 0, len(nums) - 1)
        
# @lc code=end

