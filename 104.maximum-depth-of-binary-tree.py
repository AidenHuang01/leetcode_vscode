#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def recurr(root, curr_depth):
            if not root:
                return curr_depth - 1
            left_child_depth = recurr(root.left, curr_depth + 1)
            right_child_depth = recurr(root.right, curr_depth + 1)
            return max(left_child_depth, right_child_depth)
        return recurr(root, 1)
        
# @lc code=end

