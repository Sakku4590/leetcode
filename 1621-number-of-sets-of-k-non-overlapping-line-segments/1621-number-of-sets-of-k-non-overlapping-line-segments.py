class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
    
        # dp[i][0] = 1 for all i (base case: 0 segments)
        prev = [1] * n
        
        for j in range(1, k + 1):
            curr = [0] * n
            prefix = 0  # running sum of prev[p] for p = 0..i-1
            for i in range(n):
                if i > 0:
                    curr[i] = (curr[i - 1] + prefix) % MOD
                prefix = (prefix + prev[i]) % MOD
            prev = curr
        
        return prev[n - 1]