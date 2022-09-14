#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
from typing import *
# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        max_length = 0
        longest_word = ""
        for word in strs:
            if len(word) > max_length:
                longest_word = word
                max_length = len(word)

        for i in range(len(longest_word)):
            for word in strs:
                if i == len(word) or word[i] != longest_word[i]:
                    return result
            result += longest_word[i]
        return result
# @lc code=end

