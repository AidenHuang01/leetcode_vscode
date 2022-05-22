#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        visited = {}
        global_max = 0
        i = 0
        while i < len(s):
            if s[i] in visited:
                i = visited.get(s[i]) + 1
                visited = {}
                visited[s[i]] = i
            else:
                visited[s[i]] = i
            global_max = max(len(visited), global_max)
            i += 1
        return global_max
            
        
# @lc code=end

