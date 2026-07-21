class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        """
        :type s: str
        :rtype: int
        """
        base = s.count('1')

        # Augment with 1's
        t = "1" + s + "1"

        # Run-length encoding
        runs = []
        chars = []

        i = 0
        n = len(t)
        while i < n:
            j = i
            while j < n and t[j] == t[i]:
                j += 1
            chars.append(t[i])
            runs.append(j - i)
            i = j

        ans = base

        # Look for 0 - 1 - 0 pattern
        for i in range(1, len(runs) - 1):
            if (
                chars[i] == '1'
                and chars[i - 1] == '0'
                and chars[i + 1] == '0'
            ):
                gain = runs[i - 1] + runs[i + 1]
                ans = max(ans, base + gain)

        return ans
        