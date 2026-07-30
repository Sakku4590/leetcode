class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        freq = {}

        for ch in magazine:
            freq[ch] = freq.get(ch, 0) + 1

        for ch in ransomNote:
            if freq.get(ch, 0) == 0:
                return False
            freq[ch] -= 1

        return True