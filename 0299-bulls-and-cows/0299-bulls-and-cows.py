class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull = 0
        cows = 0
        dic = {}
        s = ""
        g = ""
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
            else:
                s += secret[i]
                g += guess[i]

        for j in s:
            dic[j] = dic.get(j,0) + 1

        for h in g:
            if h in dic:
                if dic[h] > 0:
                    dic[h] -= 1
                    cows +=1
                
        return str(bull)+"A"+str(cows)+"B"
            
        