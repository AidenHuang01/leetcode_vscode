#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
from typing import *
# @lc code=start
class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.track = ""
        def backtrack(left, right):
            if left > right:
                return
            if left < 0 or right < 0:
                return 
            if left == 0 and right == 0:
                res.append(self.track)
            
            # make decision put left parenthesis
            self.track += "("
            backtrack(left-1, right)
            self.track = self.track[:-1]

            # make decision put right parenthesis
            self.track += ")"
            backtrack(left, right-1)
            self.track = self.track[:-1]
        backtrack(n, n)
        return res
            

        

    

# @lc code=end

