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
        if x == 0:
            return True
        copy = x
        revert = []
        while copy > 0:
            revert.append(copy % 10)
            copy = copy // 10
        res = ''
        for i in revert:
            res += str(i)
        return int(res) == x
        
# @lc code=end

