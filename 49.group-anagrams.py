#
# @lc app=leetcode id=49 lang=python
#
# [49] Group Anagrams
#

# @lc code=start
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        result = {}
        for str in strs:
            rep = [0] * 26
            for i in range(len(str)):
                index = ord(str[i]) - ord("a")
                rep[index] += 1
            result[rep] = result.get(rep, []).append(str)
        ans = []
        for key in result:
            ans.append(result[key])
        return ans
        
        
# @lc code=end

