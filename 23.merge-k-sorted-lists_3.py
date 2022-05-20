#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
from typing import List, Optional
from heapq import *
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__eq__ = lambda self, other: self.val == other.val
        ListNode.__lt__ = lambda self, other: self.val < other.val
        pq = []
        head = ListNode()
        tail = head
        for l in lists:
            if l:
                heappush(pq, (l.val, l))
        
        while pq:
            curr = heappop(pq)[1]
            tail.next = curr
            tail = tail.next
            if curr.next:
                heappush(pq, (curr.next.val, curr.next))
        return head.next
# @lc code=end

