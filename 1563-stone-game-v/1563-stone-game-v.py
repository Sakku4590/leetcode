class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)

        if n == 1:
            return 0

        # dp[i][j] = maximum score for stoneValue[i:j+1]
        dp = [[0] * n for _ in range(n)]

        # mx[i][j] helps us get the best value quickly
        mx = [[0] * n for _ in range(n)]

        for i in range(n):
            mx[i][i] = stoneValue[i]

        # Fix the right boundary
        for j in range(1, n):

            mid = j
            left_sum = stoneValue[j]
            right_sum = 0

            # Move left boundary backwards
            for i in range(j - 1, -1, -1):

                left_sum += stoneValue[i]

                # Move mid until left part is no longer
                # smaller than the right part
                while mid > i and (right_sum + stoneValue[mid]) * 2 <= left_sum:
                    right_sum += stoneValue[mid]
                    mid -= 1

                # Equal sums
                if right_sum * 2 == left_sum:
                    dp[i][j] = mx[i][mid]

                # Left side is smaller
                if mid != i:
                    dp[i][j] = max(
                        dp[i][j],
                        mx[i][mid - 1]
                    )

                # Right side is smaller
                if mid != j:
                    dp[i][j] = max(
                        dp[i][j],
                        mx[j][mid + 1]
                    )

                # Update helper tables
                mx[i][j] = max(
                    mx[i][j - 1],
                    dp[i][j] + left_sum
                )

                mx[j][i] = max(
                    mx[j][i + 1],
                    dp[i][j] + left_sum
                )

        return dp[0][n - 1]