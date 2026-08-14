class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = {}
        left = 0
        max_length = 0

        for right in range(len(s)):
            # Add current character
            count[s[right]] = count.get(s[right], 0) + 1

            # If current character appears more than twice,
            # shrink the window
            while count[s[right]] > 2:
                count[s[left]] -= 1
                left += 1

            # Current window is valid
            max_length = max(max_length, right - left + 1)

        return max_length