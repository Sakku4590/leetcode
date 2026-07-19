class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}
        # for count charecter
        for i,ch in enumerate(s):
            dic[ch] = i
        # create a set 
        seen = set()

        # final list
        f = []

        for i,ch in enumerate(s):
            if ch in seen:
                continue
            
            while (f and ch < f[-1] and dic[f[-1]] > i):
                seen.remove(f.pop())
            f.append(ch)
            seen.add(ch)
            
        return "".join(f)
        