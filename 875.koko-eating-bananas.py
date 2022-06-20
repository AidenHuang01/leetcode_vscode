#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#
from typing import List
import math
# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        bot = 1
        top = max(piles)
        k = 0
        while bot <= top:
            mid = (bot + top) // 2
            total = 0
            for i in piles:
                total += math.ceil(i/mid) 
            if total <= h:
                top = mid - 1
                k = mid
            else:
                bot = mid + 1
        return k
# @lc code=end

