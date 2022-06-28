#
# @lc app=leetcode id=1046 lang=python
#
# [1046] Last Stone Weight
#

# @lc code=start
import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        self.minheap = [ -x for x in stones]
        heapq.heapify(self.minheap)
        while len(self.minheap) >= 2:
            x = -heapq.heappop(self.minheap)
            y = -heapq.heappop(self.minheap)
            if x < y:
                new_stone = y - x
                heapq.heappush(self.minheap, -new_stone)
            elif x > y:
                new_stone = x - y
                heapq.heappush(self.minheap, -new_stone)
        if len(self.minheap) > 0:
            return -self.minheap[0]
        return 0

        
# @lc code=end

