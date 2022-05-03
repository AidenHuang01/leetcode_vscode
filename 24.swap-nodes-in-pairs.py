#
# @lc app=leetcode id=24 lang=python
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy_node = ListNode(next=head)
        parent =dummy_node
        while parent.next and parent.next.next:
            node_left = parent.next
            node_right = parent.next.next
            node_after = parent.next.next.next

            parent.next = node_right
            node_right.next = node_left
            node_left.next = node_after

            parent = node_left
        return dummy_node.next
        
# @lc code=end

