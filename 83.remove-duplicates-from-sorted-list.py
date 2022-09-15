#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#
from typing import *
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        dummy = head
        prev = None
        while head:
            if head.val in visited:
                prev.next = head.next
                head = head.next
            else:
                visited.add(head.val)
                prev = head
                head = head.next
        return dummy

# @lc code=end

