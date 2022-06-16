#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#
from typing import List
# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k % l
        list_1 = nums[:l-k]
        list_2 = nums[l-k:]
        print(list_1)
        print(list_2)
        # list_2.extend(list_1)
        print(list_2)
        nums[:k] = list_2
        nums[k:] = list_1
# @lc code=end

