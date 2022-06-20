#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        overflow = 0
        dummy = ListNode()
        head = dummy
        while l1 or l2:
            if l1 and l2:
                res = l1.val + l2.val + overflow
                l1 = l1.next
                l2 = l2.next
            elif l1:
                res = l1.val + overflow
                l1 = l1.next
            elif l2:
                res = l2.val + overflow
                l2 = l2.next
            overflow = res // 10
            res = res % 10
            head.next = ListNode(val=res)
            head = head.next

        if overflow != 0:
            head.next = ListNode(val=overflow)
        return dummy.next
# @lc code=end

