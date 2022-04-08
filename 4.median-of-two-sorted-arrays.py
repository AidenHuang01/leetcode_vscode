#
# @lc app=leetcode id=4 lang=python
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        len1 = len(nums1)
        len2 = len(nums2)
        len_total = len1 + len2
        len_half = len_total // 2

        left, right = 0, len(nums1) - 1
        while True:
            i = (left + right) // 2
            j = len_half - i - 2

            left_1 = nums1[i] if i >= 0 else float("-infinity")
            right_1 = nums1[i+1] if (i + 1) < len1 else float("infinity")
            left_2 = nums2[j] if j >= 0 else float("-infinity")

            right_2 = nums2[j+1] if (j + 1) < len2 else float("infinity")

            if left_1 <= right_2 and left_2 <= right_1:
                if len_total % 2:
                    return min(right_1, right_2)
                return (max(left_1, left_2) + min(right_1, right_2)) / 2.
            elif left_1 > right_2:
                right = i - 1
            else:
                left = i + 1
# @lc code=end

