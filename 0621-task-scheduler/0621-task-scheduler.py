class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        freq = Counter(tasks)

        maxFreq = max(freq.values())

        countMax = 0

        for f in freq.values():
            if f == maxFreq:
                countMax += 1

        return max(
            len(tasks),
            (maxFreq - 1) * (n + 1) + countMax
        )
        