class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        i = 1
        while True:
            product = 1
            for i in str(n):
                product *= int(i)
            if product % t == 0:
                return n
                break
            n +=1

        