class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        
        # sort indices by right endpoint
        order = sorted(range(n), key=lambda i: intervals[i][1])
        starts = [intervals[order[i]][0] for i in range(n)]
        ends   = [intervals[order[i]][1] for i in range(n)]
        weights= [intervals[order[i]][2] for i in range(n)]
        
        NEG = float('-inf')
        # dp[i][k] = (score, sorted_list_of_original_indices)
        dp = [[(NEG, []) for _ in range(5)] for _ in range(n + 1)]
        dp[0][0] = (0, [])
        
        def better(a, b):
            if a[0] != b[0]:
                return a if a[0] > b[0] else b
            return a if a[1] <= b[1] else b
        
        for i in range(1, n + 1):
            cur_start = starts[i - 1]
            cur_w = weights[i - 1]
            cur_orig = order[i - 1]
            
            # p = count of prior intervals (0..i-2) with end < cur_start
            p = bisect.bisect_left(ends, cur_start, 0, i - 1)
            
            for k in range(5):
                candA = dp[i - 1][k]
                candB = (NEG, [])
                if k >= 1 and dp[p][k - 1][0] != NEG:
                    score_b = dp[p][k - 1][0] + cur_w
                    list_b = sorted(dp[p][k - 1][1] + [cur_orig])
                    candB = (score_b, list_b)
                dp[i][k] = better(candA, candB)
        
        best = dp[n][0]
        for k in range(1, 5):
            best = better(best, dp[n][k])
        
        return best[1]