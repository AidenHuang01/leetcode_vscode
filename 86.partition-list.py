#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#
from typing import Optional
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode()
        dummy2 = ListNode()
        p1 = dummy1
        p2 = dummy2
        while head:
            if head.val < x:
                p1.next = ListNode(val = head.val)
                p1 = p1.next
            else:
                p2.next = ListNode(val = head.val)
                p2 = p2.next
            head = head.next
        p1.next = dummy2.next
        return dummy1.next
# @lc code=end

