class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        total = sum(stones)          # P[n]
        running_max = total          # dp[n] = 0  ->  g[n] = P[n]
        cur_prefix = total

        for i in range(n - 1, 1, -1):   # i = n-1 down to 2
            cur_prefix -= stones[i]     # cur_prefix = P[i]
            val = cur_prefix - running_max
            if val > running_max:
                running_max = val

        return running_max