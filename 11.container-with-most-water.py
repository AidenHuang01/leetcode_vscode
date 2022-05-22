#
# @lc app=leetcode id=11 lang=python
#
# [11] Container With Most Water
#

# @lc code=start
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Use a left and right pointer and move the smaller one
        l = 0
        r = len(height) - 1
        global_max = 0
        while l < r:
            water = min(height[l], height[r]) * (r-l)
            global_max = max(water, global_max)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return global_max

# @lc code=end

