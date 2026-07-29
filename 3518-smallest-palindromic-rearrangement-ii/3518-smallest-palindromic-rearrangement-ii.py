class Solution(object):
    def smallestPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n = len(s)
        freq = Counter(s)
        
        mid = ''
        counts = [0] * 26
        for ch, f in freq.items():
            if f % 2 == 1:
                mid = ch
            counts[ord(ch) - ord('a')] = f // 2
        
        L = n // 2  # length of the half we need to build

        def comb_capped(n_, r_, cap):
            # returns C(n_, r_) if <= cap, else cap+1 (sentinel meaning "big enough")
            r_ = min(r_, n_ - r_)
            if r_ <= 0:
                return 1
            result = 1
            for i in range(1, r_ + 1):
                result = result * (n_ - r_ + i) // i
                if result > cap:
                    return cap + 1
            return result

        def multinomial_capped(cnts, total, cap):
            # number of distinct arrangements of multiset 'cnts' (size = total), capped at 'cap'
            result = 1
            remaining = total
            for c in cnts:
                if c == 0:
                    continue
                comb = comb_capped(remaining, c, cap)
                if comb > cap:
                    return cap + 1
                result *= comb
                if result > cap:
                    return cap + 1
                remaining -= c
            return result

        # Check feasibility
        total_perms = multinomial_capped(counts, L, k)
        if total_perms < k:
            return ""

        result_half = []
        remaining_n = L
        remaining_k = k
        work = counts[:]

        for _ in range(L):
            for idx in range(26):
                if work[idx] == 0:
                    continue
                work[idx] -= 1
                cnt = multinomial_capped(work, remaining_n - 1, remaining_k)
                if cnt >= remaining_k:
                    result_half.append(chr(ord('a') + idx))
                    remaining_n -= 1
                    break
                else:
                    remaining_k -= cnt
                    work[idx] += 1  # restore, try next letter

        half_str = ''.join(result_half)
        return half_str + mid + half_str[::-1]