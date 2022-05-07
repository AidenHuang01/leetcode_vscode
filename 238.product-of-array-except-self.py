#
# @lc app=leetcode id=238 lang=python
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        init = 1 
        for i in nums[1:]:
            init *= i
        res.append(init)
        for i in range(1,len(nums)):
            if nums[i] == 0:
                special = 1
                for j in range(len(nums)):
                    if i != j:
                        special *= nums[j]
                res.append(special)
            else:
                if init != 0:
                    init = init / nums[i] * nums[i - 1]
                else:
                    init = 0
                res.append(init)
        return res
# @lc code=end

