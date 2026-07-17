class Solution(object):
    def convertToTitle(self, s):
        """
        :type columnNumber: int
        :rtype: str
        """
        dic = {
            1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 
            9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 
            16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 
            23: 'W', 24: 'X', 25: 'Y', 26: 'Z'
        }

        f = []
        if s<= 26:
            return dic[s]
        else:
            while s > 26:
                r = s//26
                m = s % 26
                if m == 0:
                    m = 26
                    r = r-1
                f.append(dic[m])
                s = r
            else:
                f.append(dic[r])
        lf = f[::-1]
        return ("".join(lf))
        