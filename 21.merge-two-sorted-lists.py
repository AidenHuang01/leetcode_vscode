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
        ptr_1 = list1
        ptr_2 = list2
        dummy = ListNode()
        curr = dummy
        while ptr_1 and ptr_2:
            if ptr_1.val < ptr_2.val:
                curr.next = ListNode(val=ptr_1.val)
                curr = curr.next
                ptr_1 = ptr_1.next
            else:
                curr.next = ListNode(val=ptr_2.val)
                curr = curr.next
                ptr_2 = ptr_2.next
        if ptr_1:
            curr.next = ptr_1
        elif ptr_2:
            curr.next = ptr_2
        return dummy.next
                
# @lc code=end

