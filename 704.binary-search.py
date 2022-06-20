#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#
from typing import List
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            # print(f"mid={mid}, l={l}, r={r}")
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
        return -1
# @lc code=end

