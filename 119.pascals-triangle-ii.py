#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        prev_row = self.getRow(rowIndex - 1)
        result = []
        for i in range(len(prev_row) - 1):
            result.append(prev_row[i] + prev_row[i+1])
        result.insert(0, 1)
        result.append(1)
        return result
        
# @lc code=end

