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

queue = []
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        curr = root
        queue.append(curr)
        res = []
        while queue:
            level = []
            for i in range(len(queue)):
                ptr = queue.pop(0)
                level.append(ptr.val)
                if ptr.left:
                    queue.append(ptr.left)
                if ptr.right:
                    queue.append(ptr.right)
            res.append(level)
        return res


# @lc code=end

