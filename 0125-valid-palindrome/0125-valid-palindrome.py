class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re

        h = re.sub(r"[^a-zA-Z0-9]", "", s).lower()

        index = h[::-1]
        if h == index:
            return True
        else:
            return False
        