#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
from typing import *
# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_length = -1
        res = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    length = j - i + 1
                    if length > max_length:
                        res = s[i:j+1]
                        max_length = length
        return res
# @lc code=end

