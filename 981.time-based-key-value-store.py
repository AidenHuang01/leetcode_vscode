#
# @lc app=leetcode id=981 lang=python
#
# [981] Time Based Key-Value Store
#
import heapq
# @lc code=start
class TimeMap(object):

    def __init__(self):
        self.tmap = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.tmap:
            self.tmap[key] = []
        heapq.heappush(self.tmap[key], (timestamp, value))
        
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.tmap:
            return ""
        record = self.tmap[key]
        res = ""
        tlist = self.tmap[key]
        l, r = 0, len(tlist) - 1
        while l <= r:
            m = (l + r) // 2
            if tlist[m][0] <= timestamp:
                res = tlist[m][1]
                l = m + 1
            else:
                r = m - 1
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end

