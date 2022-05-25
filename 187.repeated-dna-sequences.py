#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#
from typing import List
# @lc code=start
class Solution:
    # def findRepeatedDnaSequences(self, s: str) -> List[str]:
    #     left = 0
    #     right = 9
    #     result = set()
    #     while right < len(s):
    #         curr = s[left:right+1]
    #         start = left+1
    #         end = start+9
    #         while end < len(s):
    #             substring = s[start:end+1]
    #             # print('curr:     ', curr)
    #             # print('substring:', substring)
    #             if curr == substring:
    #                 result.add(curr)
    #                 break
    #             start += 1
    #             end += 1
    #         left += 1
    #         right += 1
    #     return list(result)
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        count = {}
        res = []
        for i in range(len(s)-9):
            substring = s[i:i+10]
            count[substring] = count.get(substring, 0) + 1
        for key in count.keys():
            if count[key] > 1:
                res.append(key)
        return res
# @lc code=end

