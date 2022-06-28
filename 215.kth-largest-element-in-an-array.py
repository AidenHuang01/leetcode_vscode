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
        def sort(nums, left, right):
            if len(nums) <= 1 or left >= right:
                return nums
            pivot = partition(nums, left, right)
            sort(nums, left, pivot - 1)
            sort(nums, pivot + 1, right)
            return nums
        def partition(nums, left, right):
            pivot = nums[right]
            ptr = left
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[ptr], nums[i] = nums[i], nums[ptr]
                    ptr += 1
            nums[ptr], nums[right] = nums[right], nums[ptr]
            return ptr
        nums = sort(nums, 0, len(nums) - 1)
        # print(nums)
        return nums[-k]
        
# @lc code=end

