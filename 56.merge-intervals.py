#
# @lc app=leetcode id=56 lang=python
#
# [56] Merge Intervals
#

# @lc code=start


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        record = []
        for span in intervals:
            if not record:
                record.append(span)
            else:
                if record[-1][1] >= span[0]:
                    record[-1] = [min(record[-1][0], span[0]), max(record[-1][1], span[1])]
                else:
                    record.append(span)
        return record



        
# @lc code=end

