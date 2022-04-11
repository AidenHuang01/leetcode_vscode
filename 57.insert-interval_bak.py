#
# @lc app=leetcode id=57 lang=python
#
# [57] Insert Interval
#

# @lc code=start
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        for i in range(len(intervals)):
            span = intervals[i]
            # no onverlapping
            if span[1] < newInterval[0] or newInterval[1] < span[0]:
                continue
            # ----- span
            #   ----- newInterval
            if span[0] < newInterval[0] and newInterval[0] < span[1]:
                intervals.pop(i)
                intervals.insert(i, [span[0], newInterval[1]])
                newInterval = [span[0], newInterval[1]]
            #    -----    span
            #  -----    newInterval
            elif newInterval[0] < span[0] and span[0] < newInterval[1]:
                intervals.pop(i)
                intervals.insert(i, [newInterval[0], span[1]])
                newInterval = [newInterval[0], span[1]]
            # ---------    span
            #   ----       newInterval
            elif span[0] < newInterval[0] and newInterval[1] < span[1]:
                break
            #   ----       span
            # ---------    newInterval
            elif newInterval[0] < span[0] and span[1] < newInterval[1]:
                intervals.pop(i)
                intervals.insert(i, [newInterval[0], newInterval[1]])
                newInterval = [newInterval[0], newInterval[1]]
        return intervals
# @lc code=end

