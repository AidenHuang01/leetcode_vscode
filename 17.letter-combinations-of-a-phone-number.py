#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
from typing import *
# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        mapping = {}
        mapping[2] = "abc"
        mapping[3] = "def"
        mapping[4] = "ghi"
        mapping[5] = "jkl"
        mapping[6] = "mno"
        mapping[7] = "pqrs"
        mapping[8] = "tuv"
        mapping[9] = "wxyz"

        res = []
        self.track = ""
        def backtrack(start):
            if start >= len(digits):
                res.append(self.track)
                return
            candidates = mapping[int(digits[start])]
            for i in range(len(candidates)):
                self.track += candidates[i]
                backtrack(start + 1)
                self.track = self.track[:-1]
        backtrack(0)
        return res
# @lc code=end

