#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        track = []
        def backtrack(nums, start):
            res.append(track.copy())
            for i in range(start, len(nums)):
                track.append(nums[i])
                backtrack(nums, i+1)
                track.pop()
        backtrack(nums, 0)
        return res

        
        
# @lc code=end

