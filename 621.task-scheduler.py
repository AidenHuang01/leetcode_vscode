#
# @lc app=leetcode id=621 lang=python
#
# [621] Task Scheduler
#

# @lc code=start
from heapq import heapify, heappop, heappush
from collections import Counter, deque

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # initialization
        # dict = {}
        # minheap = []
        # for i in range(len(tasks)):
        #     dict[tasks[i]] = dict.get(tasks[i], 0) + 1
        # for key in dict.keys():
        #     tup = [-dict[key], key]
        #     heappush(minheap, tup)
        # queue = []
        # res = 0
        # while len(minheap) > 0:
        #     # print(minheap)
        #     buffer = []
        #     available = True
        #     curr = heappop(minheap)
        #     while curr[1] in queue:
        #         buffer.append(curr)
        #         if len(minheap) == 0:
        #             available = False
        #             break
        #         curr = heappop(minheap)
        #     for tup in buffer:
        #         heappush(minheap, tup)
        #     if not available:
        #         queue.append("idle")
        #         res += 1
        #     else:
        #         curr[0] += 1
        #         if curr[0] < 0:
        #             heappush(minheap, curr)
        #         queue.append(curr[1])
        #         res += 1
        #     if len(queue) > n:
        #         queue.pop(0)
        # return res
        count = Counter(tasks)
        maxheap = [-x for x in count.values()]
        heapify(maxheap)
        time = 0
        queue = deque() # it stores the pair of [cnt, wakeUpTime]
        while maxheap or queue:
            time += 1
            if not maxheap:
                time = queue[0][1]
            else:
                cnt = 1 + heappop(maxheap)
                if cnt < 0:
                    queue.append([cnt, time+n])
            if queue and queue[0][1] <= time:
                heappush(maxheap, queue.popleft()[0])
            # print(time)
        return time 

# @lc code=end

