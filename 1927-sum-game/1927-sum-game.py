class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        sum1 = sum2 = cnt1 = cnt2 = 0
        
        for i in range(half):
            if num[i] == '?':
                cnt1 += 1
            else:
                sum1 += int(num[i])
        
        for i in range(half, n):
            if num[i] == '?':
                cnt2 += 1
            else:
                sum2 += int(num[i])
        
        q = cnt1 + cnt2
        if q % 2 == 1:
            return True  # Alice always wins if she has the last move
        
        diff = sum1 - sum2
        # Bob wins iff diff == 9*(cnt2-cnt1)/2  <=>  2*diff == 9*(cnt2-cnt1)
        return 2 * diff != 9 * (cnt2 - cnt1)