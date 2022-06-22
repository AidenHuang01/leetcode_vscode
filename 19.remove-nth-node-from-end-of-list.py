#
# @lc app=leetcode id=19 lang=python
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head
        if not head.next:
            return None
        dummy = ListNode(next=head)
        l, r = dummy, dummy
        for i in range(n):
            r = r.next
        while r.next:
            l = l.next
            r = r.next
        if l.next:
            l.next = l.next.next
        else:
            l.next = None
        return dummy.next
        
# @lc code=end

