#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.backTracking(result, '', 0, 0, n)
        return result

    def backTracking(self, result, str, open, close, max):
        if len(str) == 2*max:
            result.append(str)
            return
        if (open < max):
            self.backTracking(result, str + '(', open + 1, close, max)
        if (close < open):
            self.backTracking(result, str + ')', open, close + 1, max)
            

        

    

# @lc code=end

