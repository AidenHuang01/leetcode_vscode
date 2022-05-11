#
# @lc app=leetcode id=128 lang=python
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        global_max = 0
        for num in nums:
            if num - 1 not in num_set:
                local_max = 0
                curr = num
                while curr in num_set:
                    local_max += 1
                    curr += 1
                global_max = max(local_max, global_max)
        return global_max

# @lc code=end

