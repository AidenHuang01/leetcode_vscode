#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = []
        queue.append(root)
        res = []
        while queue:
            res.append(queue[-1].val)
            next_level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
            queue = next_level
        return res
        
# @lc code=end

