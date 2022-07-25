#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
from typing import *
# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
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
        def threeSum(nums, start, target):
            res = []
            ptr = start
            while ptr < len(nums):
                prev = nums[ptr]
                two_sum_res = twoSum(nums, ptr+1, target-nums[ptr])
                for group in two_sum_res:
                    sub = [nums[ptr]]
                    for n in group:
                        sub.append(n)
                    res.append(sub)
                while ptr < len(nums) and nums[ptr] == prev:
                    ptr += 1
            return res
        
        nums.sort()
        res = []
        ptr = 0
        while ptr < len(nums):
            prev = nums[ptr]
            three_sum_res = threeSum(nums, ptr+1, target-nums[ptr])
            for group in three_sum_res:
                sub = [nums[ptr]]
                for n in group:
                    sub.append(n)
                res.append(sub)
            while ptr < len(nums) and nums[ptr] == prev:
                ptr += 1
        return res
        
# @lc code=end

