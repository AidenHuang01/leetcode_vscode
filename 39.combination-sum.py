#
# @lc app=leetcode id=39 lang=python3
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
        res = []
        track = []
        track_sum = [0]
        candidates.sort()
        def backtrack(nums, start, target):
            if track_sum[0] == target:
                res.append(track.copy())
            if track_sum[0] > target:
                return
            for i in range(start, len(nums)):
                track.append(nums[i])
                track_sum[0] += nums[i]
                backtrack(nums, i, target)
                track_sum[0] -= track.pop()

                
        backtrack(candidates, 0, target)
        return res

        

        
# @lc code=end

