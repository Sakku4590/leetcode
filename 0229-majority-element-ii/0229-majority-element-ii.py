class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        n = len(nums)
        freq = Counter(nums)
        ans = []
        for num, count in freq.items():
            if count > n/3:
                ans.append(num)
                
        return ans
                