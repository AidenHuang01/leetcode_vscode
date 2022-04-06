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
        total_len = int((len(nums1)+len(nums2))/2)
        a_left = 0
        a_right = int(len(nums1)/2)
        b_left = 0
        b_right = total_len - a_right - 1
        while nums1[a_right] > nums2[b_right+1] or nums1[a_right+1] < nums2[b_right]:
            if nums1[a_right] > nums2[b_right+1]:
                b_right = int(b_right+len(nums2))
                a_right = total_len - b_right - 1
            if nums1[a_right+1] < nums2[b_right]:
                a_right = int(a_right+len(nums1))
                b_right = total_len - a_right - 1
            print(a_right)
            print(b_right)
        if total_len%2 == 0:
            return (nums1[a_right+1]+nums2[b_right+1])/2
        if nums1[a_right+1] < nums2[b_right+1]:
            return nums1[a_right+1]
        else:
            return nums2[b_right+1]

        
    
# @lc code=end

