#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#
from typing import *
# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res = [0 for i in range(len(nums2))]
        for i in range(len(nums2)-1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1]
            else:
                res[i] = -1
            stack.append(nums2[i])
        output = []
        for n in nums1:
            idx= nums2.index(n)
            output.append(res[idx])
        return output
# @lc code=end

