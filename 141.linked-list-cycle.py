#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
from typing import Optional
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        f = head
        s = head
        while f and s:
            f = f.next
            s = s.next
            if not s:
                return False
            s = s.next
            if f == s:
                return True
        return False
            
# @lc code=end

