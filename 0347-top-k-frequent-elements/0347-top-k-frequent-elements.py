class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = Counter(nums)

        top_k = count.most_common(k)

        number = [num for num, count in top_k]

        return number
        