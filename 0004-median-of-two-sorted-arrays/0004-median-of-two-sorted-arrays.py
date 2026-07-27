class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num = nums1 + nums2
        num.sort()

        if len(num) % 2 != 0:
            p = len(num) // 2
            return num[p]
        else:
            p1 = (len(num) // 2) - 1
            p2 = (len(num) // 2) 
            p = (num[p1] + num[p2]) / 2.0
            return p
        