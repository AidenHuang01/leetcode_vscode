#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(b) > len(a):
            a, b = b, a
        ptr_a = len(a) - 1
        ptr_b = len(b) - 1
        overflow = 0
        output = ""
        while ptr_a >= 0 and ptr_b >= 0:
            result = int(a[ptr_a]) + int(b[ptr_b]) + overflow
            remain = result % 2
            overflow = result // 2
            output += str(remain)
            ptr_a -= 1
            ptr_b -= 1
        while ptr_a >= 0:
            result = int(a[ptr_a]) + overflow
            remain = result % 2
            overflow = result // 2
            output += str(remain)
            ptr_a -= 1
        if overflow != 0:
            output += str(overflow)
        output = output[::-1]
        return output

# @lc code=end

