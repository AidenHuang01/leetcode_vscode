#
# @lc app=leetcode id=23 lang=python
#
# [23] Merge k Sorted Lists
#
from heapq import *
from functools import cmp_to_key
# @lc code=start
# Definition for singly-linked list.
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
        def mycmp(triplet_left, triplet_right):
            key_l, key_r = triplet_left.val, triplet_right.val
            if key_l < key_r:
                return -1  # larger first
            elif key_l == key_r:
                return 0  # equal
            else:
                return 1
        WrapperCls = cmp_to_key(mycmp)
        pq = []
        dummy = ListNode()
        curr = dummy
        for list in lists:
            if list:
                heappush(pq, WrapperCls(list))
        while pq:
            node = heappop(pq).obj
            curr.next = node
            curr = curr.next
            if node.next:
                heappush(pq, WrapperCls(node.next))
        return dummy.next


        
# @lc code=end

