#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pos_dict = {}
        for i in range(len(nums)):
            if target - nums[i] not in pos_dict:
                pos_dict[nums[i]] = i
            else:
                return [pos_dict[target - nums[i]], i] 
# @lc code=end

