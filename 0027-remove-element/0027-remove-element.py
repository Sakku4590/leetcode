class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        lis = []

        for x in nums:
            if x != val:
                lis.append(x)

        nums[:len(lis)] = lis

        return len(lis)

        