#
# @lc app=leetcode id=39 lang=python
#
# [39] Combination Sum
#

# @lc code=start
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        valid = False
        for i in candidates:
            if i <= target:
                valid = True
        print(valid)
        if not valid:
            return None
        for i in candidates:
            if i < target:
                print(target - i)
                sub = self.combinationSum(candidates, target - i)
                if sub:
                    for ans in sub:
                        ans.append(i)
        for i in candidates:
            if i == target:
                return [i]
# @lc code=end

