#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        l, r = 0, x
        while l <= r:
            mid = (l + r) // 2
            print(f"mid = {mid}, l = {l}, r = {r}")

            if mid ** 2 == x:
                return mid
            if mid ** 2 < x:
                if (mid+1) ** 2 > x:
                    return mid
                else:
                    l = mid + 1
            else:
                r = mid - 1
# @lc code=end

