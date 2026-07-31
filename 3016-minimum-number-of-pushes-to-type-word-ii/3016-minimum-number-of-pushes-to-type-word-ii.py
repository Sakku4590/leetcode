class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        freq = list(Counter(word).values())
        freq.sort(reverse=True)

        ans = 0

        for i, f in enumerate(freq):
            ans += f * (i // 8 + 1)

        return ans
        