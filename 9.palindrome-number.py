#
# @lc app=leetcode id=9 lang=python
#
# [9] Palindrome Number
#

# @lc code=start




class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        digits = []
        while x > 0:
            digits.append(x % 10)
            x = x // 10
        l, r = 0, len(digits) - 1
        while l < r:
            if digits[l] != digits[r]:
                return False
            l += 1
            r -= 1
        return True

        
# @lc code=end

