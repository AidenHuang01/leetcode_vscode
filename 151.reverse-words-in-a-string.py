#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start




class Solution:
    def reverseWords(self, s: str) -> str:
        l = len(s) - 1
        r = l
        res = ''
        while l >= 0 and r >= 0:
            while s[l] == ' ' and l >= 0:
                l -= 1
                r = l
            while s[l] != ' ' and l >= 0:
                l -= 1
            if l < 0:
                if r < 0:
                    break
                l = 0
                word = s[l:r+1]
                res += word + ' '
                print(f"1word={word} l={l} r={r}")
                break
            if l < 0 or r < 0:
                break
            if l == 0 and r == 0 and s[l] == ' ' and s[r] == ' ':
                break
            word = s[l+1:r+1]
            res += word + ' '   
            print(f"2word={word} l={l} r={r}")

        res = res[:-1]
        return res

# @lc code=end

