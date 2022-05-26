#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        l = 0
        max_length = 0
        for r in range(len(s)):
            idx_r = ord(s[r]) - 65
            count[idx_r] += 1
            while sum(count) - max(count) > k:
                idx_l = ord(s[l]) - 65
                count[idx_l] -= 1
                l += 1
            max_length = max(max_length, r-l+1)
        return max_length
            

# @lc code=end

