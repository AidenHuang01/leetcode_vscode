#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        translation = {"I":1, "IV":4, "V":5, "IX":9,
                       "X":10, "XL":40, "L":50, "XC":90,
                       "C":100, "CD":400, "D":500, "CM":900,
                       "M":1000}
        keys = list(translation.keys())
        keys.reverse()
        result = 0
        i = 0
        while i < len(keys):
            length = len(keys[i])
            # print(f"i={i}, {keys[i]}={translation[keys[i]]}")
            if len(s) >= length and s[:length] == keys[i]:
                result += translation[keys[i]]
                s = s[length:]
                i -= 1
            i += 1
        return result
        
# @lc code=end

