class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        seen = set(nums)
        for i in seen:
            if nums.count(i) > n/2:
                return i
                break

        