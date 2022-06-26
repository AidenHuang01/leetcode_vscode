#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
from typing import *
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def recurr(root, left_bound, right_bound):
            if not root:
                return True
            if root.val <= left_bound or root.val >= right_bound:
                return False
            return recurr(root.left, left_bound, root.val) and recurr(root.right, root.val, right_bound)
        return recurr(root, float('-inf'), float('inf'))
# @lc code=end

