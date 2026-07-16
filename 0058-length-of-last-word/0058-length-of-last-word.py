class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        w = s.split()
        # if not w:
        #     return 0
            
        return len(w[-1])