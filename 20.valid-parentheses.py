#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        visited = []
        for i in range(len(s)):
            if s[i] in ['(', '{', '[']:
                visited.append(s[i])
            else:
                if s[i] == ')':
                    if len(visited) == 0 or visited.pop() != '(':
                        return False
                if s[i] == '}':
                    if len(visited) == 0 or visited.pop() != '{':
                        return False
                if s[i] == ']':
                    if len(visited) == 0 or visited.pop() != '[':
                        return False
        return len(visited) == 0
# @lc code=end

