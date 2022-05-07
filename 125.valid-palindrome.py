#
# @lc app=leetcode id=125 lang=python
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        str_list = []
        s = s.lower()
        for i in range(len(s)):
            if s[i] > 'a' and s[i] < 'z':
                str_list.append(s[i])
        left = 0
        right = len(str_list) - 1
        while left < right:
            if str_list[left] != str_list[right]:
                return False
            left += 1
            right -= 1
        return True
                     
# @lc code=end

