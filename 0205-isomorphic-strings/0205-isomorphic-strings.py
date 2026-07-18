class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        s_to_t = {}
        t_to_s = {}

        for i in range(len(s)):
            ch1 = s[i]
            ch2 = t[i]

            if ch1 in s_to_t:
                if s_to_t[ch1] != ch2:
                    return False
            else:
                s_to_t[ch1] = ch2

            if ch2 in t_to_s:
                if t_to_s[ch2] != ch1:
                    return False
            else:
                t_to_s[ch2] = ch1

        return True