class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l = []
        longest = 0

        for ch in s:
            while ch in l:
                l.pop(0)

            l.append(ch)

            if len(l) > longest:
                longest = len(l)

        return longest
        