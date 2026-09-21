class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k
        dp = [0] * k  
        
        for num in nums:
            a = num % k
            new_dp = [0] * k
            for r in range(k):
                if dp[r]:
                    nr = (r * a) % k
                    new_dp[nr] += dp[r]
            new_dp[a] += 1  # the subarray consisting of just this element
            dp = new_dp
            
            for r in range(k):
                result[r] += dp[r]
        
        return result