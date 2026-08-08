class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        for i in range(len(nums)+1):
            if i not in nums:
                return i
        