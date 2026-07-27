class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        digits = [i for i in nums]
        digits.sort(reverse = True)
        return ((digits[0] - 1) * (digits[1] - 1))
        