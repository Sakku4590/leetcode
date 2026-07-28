class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = Counter(s)

        first = []
        middle = ""

        for ch in "abcdefghijklmnopqrstuvwxyz":
            first.append(ch * (freq[ch] // 2))
            if freq[ch] % 2 == 1:
                middle = ch

        first = "".join(first)

        return first + middle + first[::-1]
        