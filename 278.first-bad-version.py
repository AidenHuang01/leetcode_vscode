#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.


# def isBadVersion(version: int) -> bool:
#     return True
class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 0, n
        while l <= r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                if mid-1 < 0 or not isBadVersion(mid-1):
                    return mid
                else:
                    r = mid - 1
            else:
                l = mid + 1
        return -1
# @lc code=end

