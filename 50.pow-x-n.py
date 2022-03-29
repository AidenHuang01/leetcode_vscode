#
# @lc app=leetcode id=50 lang=python
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        result = 1
        for _ in range(abs(n)):
            result *= x
        if n >= 0:
            return result
        else:
            return 1/result

# @lc code=end

