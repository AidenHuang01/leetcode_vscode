#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
from typing import List
# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        total = set(nums)
        visited = set()
        longest = 0
        for num in nums:
            if (num-1) not in total and num not in visited:
                visited.add(num)
                curr = num
                local_longest = 1
                while (curr+1) in total:
                    local_longest += 1
                    curr += 1
                    visited.add(curr)
                longest = max(longest, local_longest)
        return longest
# @lc code=end

