#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start


class Node():
    def __init__(self, key=-1, val=-1, next=None, pre=None):
        self.key = key
        self.val = val
        self.next = next
        self.pre = pre
class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head
        # cache: key -> Node(val=value)
        self.cache = {}
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            node.pre.next = node.next
            node.next.pre = node.pre
            node.next = self.head.next
            node.pre = self.head
            self.head.next = node
            node.next.pre = node
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.cache[key].pre.next = self.cache[key].next
            self.cache[key].next.pre = self.cache[key].pre
        elif len(self.cache) >= self.cap:
            oldest_key = self.tail.pre.key
            self.tail.pre.pre.next = self.tail
            self.tail.pre = self.tail.pre.pre
            del self.cache[oldest_key]
        if key in self.cache:
            new_node = self.cache[key]
        else:
            new_node = Node(key, value)
            self.cache[key] = new_node
        new_node.next = self.head.next
        new_node.pre = self.head
        self.head.next = new_node
        new_node.next.pre = new_node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

