class Solution(object):
    def maxActiveSectionsAfterTrade(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(s)
        starts, ends = [], []
        i = 0
        while i < n:
            if s[i] == '1':
                j = i
                while j < n and s[j] == '1':
                    j += 1
                starts.append(i); ends.append(j-1)
                i = j
            else:
                i += 1
        m = len(starts)
        totalOnes = sum(e - st + 1 for st, e in zip(starts, ends))

        prevZero = [0]*m
        nextZero = [0]*m
        for k in range(m):
            prevEnd = ends[k-1] if k > 0 else -1
            prevZero[k] = starts[k] - prevEnd - 1
            nextStart = starts[k+1] if k < m-1 else n
            nextZero[k] = nextStart - ends[k] - 1
        base = [prevZero[k] + nextZero[k] for k in range(m)]

        # precompute floor(log2(x)) for x from 1..m using bit_length (no math.log2 needed)
        LOG = [0] * (m + 1)
        for x in range(2, m + 1):
            LOG[x] = LOG[x >> 1] + 1

        if m > 0:
            sp = [base[:]]
            jexp = 1
            while (1 << jexp) <= m:
                prev = sp[-1]
                half = 1 << (jexp-1)
                cur = [max(prev[idx], prev[idx+half]) for idx in range(m - (1<<jexp) + 1)]
                sp.append(cur)
                jexp += 1

            def rangeMax(l, r):
                if l > r:
                    return float('-inf')
                length = r - l + 1
                k = LOG[length]
                return max(sp[k][l], sp[k][r - (1 << k) + 1])
        else:
            def rangeMax(l, r):
                return float('-inf')

        ans = []
        for l, r in queries:
            if m == 0:
                ans.append(totalOnes); continue
            p = bisect.bisect_right(starts, l)
            q = bisect.bisect_left(ends, r) - 1
            if p > q or p >= m or q < 0:
                ans.append(totalOnes)
                continue
            if p == q:
                A = min(prevZero[p], starts[p] - l)
                B = min(nextZero[p], r - ends[p])
                gain = A + B
            else:
                gain_p = min(prevZero[p], starts[p] - l) + nextZero[p]
                gain_q = prevZero[q] + min(nextZero[q], r - ends[q])
                mid = rangeMax(p+1, q-1)
                gain = max(gain_p, gain_q, mid)
            ans.append(totalOnes + max(0, gain))
        return ans