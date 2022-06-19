#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#
from typing import List

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if s != "+" and s != "-" and s != "*" and s != "/":
                stack.append(int(s))
            else:
                a = stack.pop()
                b = stack.pop()
                if s == "+":
                    stack.append(b + a)
                elif s == "-":
                    stack.append(b - a)
                elif s == "*":
                    stack.append(b * a)
                elif s == "/":
                    stack.append(int(b / a))
        return stack.pop()
# @lc code=end

