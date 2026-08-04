class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        smallest = nums[0]
        largest = nums[-1]
        l = []
        i = smallest
        while i < largest:
            if i not in nums:
                l.append(i)
            i +=1
        return l
        