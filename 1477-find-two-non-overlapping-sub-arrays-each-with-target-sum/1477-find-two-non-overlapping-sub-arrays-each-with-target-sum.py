class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        INF = float('inf')
        dp = [INF] * (n + 1)  # dp[i]: min length of valid subarray fully within arr[0..i-1]
        
        ans = INF
        left = 0
        cur_sum = 0
        
        for right in range(n):
            cur_sum += arr[right]
            
            while cur_sum > target:
                cur_sum -= arr[left]
                left += 1
            
            # carry forward best length found so far (using elements up to index 'right')
            dp[right + 1] = dp[right]
            
            if cur_sum == target:
                length = right - left + 1
                if dp[left] != INF:
                    ans = min(ans, dp[left] + length)
                dp[right + 1] = min(dp[right + 1], length)
        
        return ans if ans != INF else -1