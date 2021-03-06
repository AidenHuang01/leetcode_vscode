#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
from typing import Optional
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        res = head
        while list1 or list2:
            if list1 is None:
                head.next = ListNode(list2.val)
                head = head.next
                list2 = list2.next
            elif list2 is None:
                head.next = ListNode(list1.val)
                head = head.next
                list1 = list1.next
            elif list1.val < list2.val:
                head.next = ListNode(list1.val)
                head = head.next
                list1 = list1.next
            else:
                head.next = ListNode(list2.val)
                head = head.next
                list2 = list2.next
        return res.next

# @lc code=end

