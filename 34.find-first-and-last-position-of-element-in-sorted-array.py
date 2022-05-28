#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
from typing import List

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res_l, res_r = -1, -1
        l, r = 0, len(nums)-1
        # search for res_l
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                if mid-1 < 0 or nums[mid-1] != target:
                    res_l = mid
                    break
                else:
                    r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                # print(f"mid: {mid}")
                if mid+1 >= len(nums) or nums[mid+1] != target:
                    res_r = mid
                    break
                else:
                    l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return [res_l, res_r]
                
                
# @lc code=end

