#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#
from typing import *
# @lc code=start
class Solution:
    def grayCode(self, n: int) -> List[int]:
        visited = set()
        result = []
        def list2num(nums):
            result = 0
            for i in range(len(nums)-1, -1, -1):
                result += nums[i] * 2**i
            return result

        def backtrack(path):
            result.append(list2num(path))
            visited.add(tuple(path))
            for i in range(len(path)):
                if path[i] == 0:
                    path[i] = 1
                    if tuple(path) not in visited:
                        backtrack(path)
                    path[i] = 0
                else:
                    path[i] = 0
                    if tuple(path) not in visited:
                        backtrack(path)
                    path[i] = 1

        path = [0 for i in range(n)]
        backtrack(path)
        return result
# @lc code=end

