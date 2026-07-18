class Solution(object):
    def wordPattern(self, p, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        sd = {}
        wc = {}
        s = s.split(" ")
        if len(p) != len(s):
            return False
        else:
            for ch,word in zip(p,s):
                    
                if ch in sd:
                    if sd[ch] != word:
                        return False
                else:
                    sd[ch] = word
                    
                if word in wc:
                    if wc[word] != ch:
                        return False
                else:
                    wc[word] = ch
        return True
        