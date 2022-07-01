#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#
from typing import *
# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        track = []
        def backtrack(start, s):
            if start >= len(s):
                res.append(track.copy())
            for i in range(start, len(s)):
                if s[start: i+1] == s[start: i+1][::-1]:
                    track.append(s[start: i+1])
                    backtrack(i+1, s)
                    track.pop()
        backtrack(0, s)
        return res
# @lc code=end

