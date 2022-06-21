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
        dummy_head = Node()
        dummy_tail = Node()
        cache = {}
        cap = 2

    def get(self, key: int) -> int:
        

    def put(self, key: int, value: int) -> None:
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

