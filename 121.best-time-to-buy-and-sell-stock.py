#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
# @lc code=start
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        global_max = 0
        while l <= r:
            if r == len(prices) - 1:
                return global_max
            if l == r:
                r += 1
            elif prices[l] > prices[r]:
                l = r
            else:
                r += 1
            global_max = max(prices[r]-prices[l], global_max)
        return global_max
            

# @lc code=end

