#
# @lc app=leetcode id=160 lang=python
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        ptr1 = headA
        ptr2 = headB
        while ptr1 != ptr2:
            ptr1 = ptr1.next if ptr1 else headB
            ptr2 = ptr2.next if ptr2 else headA
        return ptr1

# @lc code=end

