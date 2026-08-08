class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(len(nums)):
            m = max(nums[:i+1])
            mi = min(nums[i:])
            if m - mi <= k:
                return i
        return -1
        