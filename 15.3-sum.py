#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
from typing import *
# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(nums, start, target):
            l, r = start, len(nums) - 1
            res = []
            while l < r:
                sum = nums[l] + nums[r]
                left, right = nums[l], nums[r]
                if sum < target:
                    while l < r and nums[l] == left:
                        l += 1
                elif sum > target:
                    while l < r and nums[r] == right:
                        r -= 1
                elif sum == target:
                    res.append([nums[l], nums[r]])
                    while l < r and nums[l] == left:
                        l += 1
                    while l < r and nums[r] == right:
                        r -= 1
            return res
        nums.sort()
        ptr = 0
        output = []
        # print(nums)
        while ptr < len(nums):
            prev = nums[ptr]
            two_sum_res = twoSum(nums, ptr+1, -prev)
            # print(f"ptr={ptr}, {two_sum_res}")
            for group in two_sum_res:
                sub = [nums[ptr]]
                for n in group:
                    sub.append(n)
                output.append(sub)
            while ptr < len(nums) and nums[ptr] == prev:
                ptr += 1
        return output
                      
# @lc code=end

