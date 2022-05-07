#
# @lc app=leetcode id=347 lang=python
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # dict = {}
        # freq = [[] for i in range(len(nums) + 1)]
        # for i in nums:
        #     loc = dict.get(i, 0)
        #     dict[i] = loc + 1
        #     if i in freq[loc]:
        #         freq[loc].remove(i)
        #     freq[loc+1].append(i)
        # res = []
        # for i in reversed(freq):
        #     if k == 0:
        #         break
        #     if i:
        #         for num in i:
        #             res.append(num)
        #             k -= 1
        # return res

        dict = {}
        freq = [[] for i in range(len(nums) + 1)]
        res = []
        for i in nums:
            dict[i] = dict.get(i, 0) + 1
        for key, v in dict.items():
            freq[v].append(key)
        for i in range(len(freq)-1, 0, -1):
            if k == 0:
                return res
            if freq[i]:
                for num in freq[i]:
                    res.append(num)
                    k -= 1
        return res

        
# @lc code=end

