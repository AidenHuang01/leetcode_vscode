#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        reversed_s = s[::-1]
        ptr = 0
        counter = 0
        while ptr < len(reversed_s) and reversed_s[ptr] == " ":
            ptr += 1
        while ptr < len(reversed_s) and reversed_s[ptr] != " ":
            counter += 1
            ptr += 1
        return counter
            
        
# @lc code=end

