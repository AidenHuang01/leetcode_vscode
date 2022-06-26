#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        cap = [0]
        cap[0] = k
        def preorder(root):
            if not root:
                return
            preorder(root.left)
            if len(res) == cap[0]:
                return
            # print(f"res = {res}")
            res.append(root.val)
            preorder(root.right)
        preorder(root)
        return res[-1]
# @lc code=end

