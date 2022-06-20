#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#
from typing import Optional
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        l, r = 0, len(nodes) - 1
        while l < r:
            nodes[l].next = nodes[r]
            if l + 1 < r:
                nodes[r].next = nodes[l+1]
            else:
                nodes[r].next = None
            l += 1
            r -= 1
        if l == r:
            nodes[l].next = None
        
# @lc code=end

