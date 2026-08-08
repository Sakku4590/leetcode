class Solution(object):
    def validSequence(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: List[int]
        """
        n1, n2 = len(word1), len(word2)
        
        # back[i] = max # of trailing chars of word2 matchable as subsequence in word1[i:]
        back = [0] * (n1 + 1)
        j = n2 - 1
        for i in range(n1 - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                j -= 1
            back[i] = n2 - 1 - j
        
        result = []
        i = 0
        jj = 0
        used = False
        
        while jj < n2 and i < n1:
            if word1[i] == word2[jj]:
                result.append(i)
                i += 1
                jj += 1
            else:
                if not used and back[i + 1] >= n2 - jj - 1:
                    result.append(i)
                    i += 1
                    jj += 1
                    used = True
                else:
                    i += 1
        
        if jj < n2:
            return []
        return result
        