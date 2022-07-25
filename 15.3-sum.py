#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
from typing import *
# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def twoSum(nums, curr, target):
            l, r = 0, len(nums) - 1
            res = []
            while l < r:
                left = nums[l]
                right = nums[r]
                if l == curr:
                    l += 1
                    continue
                if r == curr:
                    r -= 1
                    continue
                two_sum = nums[l] + nums[r]
                if two_sum == target:
                    res.append([nums[l], nums[r]])
                    while l < r and nums[l] == left:
                        l += 1
                    while l < r and nums[r] == right:
                        r -= 1
                elif two_sum < target:
                    while l < r and nums[l] == left:
                        l += 1
                elif two_sum > target:
                    while l < r and nums[r] == right:
                        r -= 1
            return res
        ptr = 0
        output = set()
        while ptr < len(nums):
            prev = nums[ptr]
            two_sum_res = twoSum(nums, ptr, -prev)
            for group in two_sum_res:
                sub = [prev]
                for n in group:
                    sub.append(n)
                sub.sort()
                tup = tuple(sub)
                output.add(tup)
            while ptr < len(nums) and nums[ptr] == prev:
                ptr += 1
        res = []
        for tup in output:
            res.append(list(tup))
        return res
                
# @lc code=end

