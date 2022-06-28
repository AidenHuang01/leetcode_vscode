#
# @lc app=leetcode id=973 lang=python
#
# [973] K Closest Points to Origin
#

# @lc code=start
from math import sqrt
from heapq import heappop, heappush


class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        minheap = []
        for point in points:
            dis = sqrt(point[0]**2 + point[1]**2)
            tup = (dis, point[0], point[1])
            heappush(minheap, tup)
        res = []
        for i in range(k):
            tup = heappop(minheap)
            res.append([tup[1], tup[2]])
        return res
# @lc code=end

