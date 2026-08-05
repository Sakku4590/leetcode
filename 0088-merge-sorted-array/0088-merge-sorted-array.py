class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        ou = []
        for i in range(m):
            ou.append(nums1[i])
        for i in range(n):
            ou.append(nums2[i])
        ou.sort()
        for i in range(m+n):
            nums1[i] = ou[i]