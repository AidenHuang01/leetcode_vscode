#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
# @lc code=start
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_profit = 0
        for i in range(len(prices)):
            max_profit = max(max_profit, prices[i] - prices[l])
            while prices[l] > prices[i]:
                l += 1
        return max_profit
            

# @lc code=end

