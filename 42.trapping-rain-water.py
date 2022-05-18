#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
from typing import List
# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        max_l, max_r = height[0], height[-1]
        rain = 0
        while l < r:
            if max_l < max_r:
                curr = l + 1
                l += 1
                max_l = max(height[l], max_l)
            else:
                curr = r - 1
                r -= 1
                max_r = max(height[r], max_r)
            curr_rain = max(0, min(max_l, max_r)-height[curr])
            print("rain: %d curr: %d max_l: %d max_r %d " % (curr_rain, curr, max_l, max_r))
            rain += max(0, min(max_l, max_r)-height[curr])
        return rain






            

# @lc code=end

        # if len(height) < 3:
        #     return 0
        # while height[0] == 0:
        #     height.pop(0)
        # for i in range(len(height)-1, 1, -1):
        #     if height[i-1] > height[i]:
        #         height.pop(-1)
        #     else:
        #         break
        # if len(height) < 3:
        #     return 0
        # print(height)
        # l, r = 0, 0
        # block = []
        # rain = 0
        # print(height)
        # while l < len(height) and r < len(height):
        #     if r + 1 >= len(height):
        #         if l < r:
        #             edge = min(height[l],height[r])
        #             for i in range(len(block)):
        #                 if block[i] > edge:
        #                     block[i] = edge
        #             rain += min(height[l],height[r]) * (r-l-1) - sum(block)
        #         print("trapped ", min(height[l],height[r]) * (r-l-1) - sum(block), " l: ", l, " r: ", r, " block", block)
        #         return rain
        #     if height[r+1] >= height[l] or height[r+1]:
        #         r += 1
        #         if l < r:
        #             edge = min(height[l],height[r])
        #             for i in range(len(block)):
        #                 if block[i] > edge:
        #                     block[i] = edge
        #             rain += min(height[l], height[r]) * (r-l-1) - sum(block)
        #         print("trapped ", min(height[l],height[r]) * (r-l-1) - sum(block), " l: ", l, " r: ", r, " block", block)
        #         l = r
        #         block = []
        #     elif r+1 == len(height)-1:
        #         r += 1
        #         if l < r:
        #             edge = min(height[l],height[r])
        #             for i in range(len(block)):
        #                 if block[i] > edge:
        #                     block[i] = edge
        #             rain += min(height[l],height[r]) * (r-l-1) - sum(block)
        #         print("trapped ", min(height[l],height[r]) * (r-l-1) - sum(block), " l: ", l, " r: ", r, " block", block)
        #         return rain
        #     else:
        #         # print(r)
        #         r += 1
        #         # print("block: ", block, " r", r)
        #         block.append(height[r])
        # return rain
