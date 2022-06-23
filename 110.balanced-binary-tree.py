#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = [True]
        def dfs(root):
            if not root:
                return 0
            left_depth = dfs(root.left)
            right_depth = dfs(root.right)
            if abs(left_depth-right_depth) > 1:
                res[0] = False
            return max(left_depth, right_depth) + 1
        dfs(root)
        return res[0]
# @lc code=end

