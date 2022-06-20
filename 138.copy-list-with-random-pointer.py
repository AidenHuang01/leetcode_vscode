#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

from typing import Optional
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        new_nodes = [None] * len(nodes)
        for i in range(len(nodes)):
            node = nodes[i]
            new_nodes[i] = Node(node.val)
        for i in range(len(new_nodes)):
            if i < len(new_nodes) - 1:
                new_nodes[i].next = new_nodes[i+1]
            if nodes[i].random:
                random_idx = nodes.index(nodes[i].random)
                new_nodes[i].random = new_nodes[random_idx]
            else:
                new_nodes[i].random = None
        return new_nodes[0]

# @lc code=end

