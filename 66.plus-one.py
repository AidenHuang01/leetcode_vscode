#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
from typing import *
# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        overflow = 1
        for i in range(len(digits) - 1, -1, -1):
            result = digits[i] + overflow
            remain = result % 10
            overflow = result // 10
            digits[i] = remain
        if overflow != 0:
            digits.insert(0, overflow)
        return digits
# @lc code=end

