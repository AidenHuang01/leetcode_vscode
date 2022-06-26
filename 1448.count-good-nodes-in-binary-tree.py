#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]
        def recurr(root, par_max):
            if not root:
                return
            if root.val >= par_max:
                res[0] += 1
                par_max = root.val
            recurr(root.left, par_max)
            recurr(root.right, par_max)
        
        recurr(root, float('-inf'))
        return res[0]
# @lc code=end

