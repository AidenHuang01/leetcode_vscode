#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
from typing import List
# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [-1] * len(temperatures)
        # print(res)
        for i in range(len(temperatures) - 1, -1, -1):
            # if stack is empty, add the temperature in the stack
            if not stack:
                stack.append((temperatures[i], i))
                res[i] = 0
            else:
                while stack:
                    curr = stack.pop()
                    if temperatures[i] < curr[0]:
                        stack.append(curr)
                        res[i] = curr[1] - i
                        stack.append((temperatures[i], i))
                        break
                if not stack:
                    stack.append((temperatures[i], i))
                    res[i] = 0
        # print(res)
        return res
# @lc code=end

