class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt0 = 0
        cnt1 = 0
        cnt2 = 0

        for stone in stones:
            if stone % 3 == 0:
                cnt0 += 1
            elif stone % 3 == 1:
                cnt1 += 1
            else:
                cnt2 += 1

        # Case 1: even number of 0-remainder stones
        if cnt0 % 2 == 0:
            return cnt1 > 0 and cnt2 > 0

        # Case 2: odd number of 0-remainder stones
        return abs(cnt1 - cnt2) > 2