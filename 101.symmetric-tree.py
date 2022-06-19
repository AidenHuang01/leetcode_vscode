#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#
from typing import Optional
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root, root)
    def isMirror(self, p, q):
        if not p and not q:
            return True
        return p and q and p.val == q.val and self.isMirror(p.left, q.right) and self.isMirror(p.right, q.left)
# @lc code=end

