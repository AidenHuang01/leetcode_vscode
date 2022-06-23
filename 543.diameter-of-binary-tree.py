#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def dfs(root):
            if not root:
                return -1
            left_depth = dfs(root.left)
            right_depth = dfs(root.right)
            res[0] = max(res[0], left_depth+right_depth+2)
            return max(left_depth, right_depth) + 1
        dfs(root)
        return res[0]




# @lc code=end

