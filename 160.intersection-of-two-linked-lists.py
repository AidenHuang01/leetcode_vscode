#
# @lc app=leetcode id=160 lang=python
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None



class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        hashSetA = set()
        listA = headA
        listB = headB
        while listA:
            hashSetA.add(listA)
            listA = listA.next
        while listB:
            if listB in hashSetA:
                return listB
            listB = listB.next

# @lc code=end

