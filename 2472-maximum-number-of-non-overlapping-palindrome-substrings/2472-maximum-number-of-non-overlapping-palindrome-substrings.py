class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        if n < k:
            return 0
        
        # Precompute palindrome table
        pal = [[False] * n for _ in range(n)]
        for i in range(n):
            pal[i][i] = True
        for i in range(n - 1):
            pal[i][i + 1] = (s[i] == s[i + 1])
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                pal[i][j] = (s[i] == s[j]) and pal[i + 1][j - 1]
        
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1]
            # length k window ending at i
            if i >= k and pal[i - k][i - 1]:
                dp[i] = max(dp[i], dp[i - k] + 1)
            # length k+1 window ending at i
            if i >= k + 1 and pal[i - k - 1][i - 1]:
                dp[i] = max(dp[i], dp[i - k - 1] + 1)
        
        return dp[n]