#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(A, B):
            if not A and not B:
                return True
            if not (A and B):
                return False
            if A.val != B.val:
                return False
            return check(A.left, B.left) and check(A.right, B.right)
        return bool(root and subRoot) and (check(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
# @lc code=end

