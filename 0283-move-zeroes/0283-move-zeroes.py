class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        ans = []
        count = 0
        
        for i in nums:
            if i != 0:
                ans.append(i)
            if i == 0:
                count += 1

        ans.extend([0] * count)
        nums[:] = ans
        