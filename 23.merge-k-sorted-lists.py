#
# @lc app=leetcode id=23 lang=python
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
from heapq import *
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        pq = []
        head = ListNode()
        tail = head
        for list in lists:
            if list:
                heappush(pq, (list.val, list))
        
        while pq:
            curr = heappop(pq)[1]
            tail.next = curr
            tail = tail.next
            if curr.next:
                heappush(pq, (curr.next.val, curr.next))
        return head.next
# @lc code=end

