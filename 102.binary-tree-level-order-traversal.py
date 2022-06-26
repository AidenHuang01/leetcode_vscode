#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = []
        queue.append(root)
        res = []
        while queue:
            new_line = []
            for node in queue:
                new_line.append(node.val)
            res.append(new_line)
            level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.left: level.append(node.left) 
                if node.right: level.append(node.right)
            queue = level
        return res



# @lc code=end

