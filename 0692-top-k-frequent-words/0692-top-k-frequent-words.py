class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count = Counter(words)
        return sorted(
            count.keys(),
            key=lambda x: (-count[x], x)
        )[:k]
        