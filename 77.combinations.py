#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#
from typing import *
# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        track = []
        self.n = n
        self.k = k
        def backtrack(start):
            if len(track) == self.k:
                res.append(track.copy())
                return
            for i in range(start, self.n+1):
                track.append(i)
                backtrack(i+1)
                track.pop()
        backtrack(1)
        return res
# @lc code=end

