#
# @lc app=leetcode id=53 lang=python
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution of O(n)
        curr_sum = max_sum = nums[0]
        for i in nums[1:]:
            if curr_sum < 0:
                curr_sum = i
            else:
                curr_sum += i
            max_sum = max(curr_sum, max_sum)
        return max_sum

        # Solution of O(n**2)
        # global_max = float('-inf')
        # for i in range(len(nums)):
        #     max_sum = float('-inf')
        #     curr_sum = 0
        #     for j in range(i, len(nums)):
        #         curr_sum += nums[j]
        #         max_sum = max(curr_sum, max_sum)
        #     global_max = max(max_sum, global_max)
        # return global_max
# @lc code=end

