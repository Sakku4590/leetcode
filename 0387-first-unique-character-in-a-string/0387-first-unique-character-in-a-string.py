class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for i in s:
            dic[i] = dic.get(i,0) +1
        for k,v in enumerate(s):
            if dic[v] == 1:
                return k
        return -1

        