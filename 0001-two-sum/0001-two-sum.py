class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}

        for current_index, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return seen[complement],current_index

            seen[num] = current_index
        return []

        