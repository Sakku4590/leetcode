class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = [0]*26
        for ch in s:
            cnt[ord(ch)-97] += 1
        odd_chars = [c for c in range(26) if cnt[c] % 2 == 1]

        if n % 2 == 0:
            if len(odd_chars) != 0:
                return ""
            mid = None
        else:
            if len(odd_chars) != 1:
                return ""
            mid = odd_chars[0]

        half = [cnt[c] // 2 for c in range(26)]
        h = (n + 1) // 2
        T = target
        Tprefix = T[:h]

        # ---- candidate a: H == target[:h] exactly ----
        candidate_a = None
        if n % 2 == 0:
            tc = [0]*26
            for ch in Tprefix:
                tc[ord(ch)-97] += 1
            if tc == half:
                H = Tprefix
                P = H + H[::-1]
                if P > T:
                    candidate_a = P
        else:
            Hfree_target = Tprefix[:h-1]
            tc = [0]*26
            for ch in Hfree_target:
                tc[ord(ch)-97] += 1
            if tc == half and (ord(Tprefix[h-1]) - 97 == mid):
                H = Tprefix
                P = H + Hfree_target[::-1]
                if P > T:
                    candidate_a = P

        # ---- candidate b: smallest H strictly greater than target[:h] ----
        remaining = half[:]
        best_pos, best_char, best_snapshot = -1, -1, None
        broke = False
        free_positions = range(h-1) if n % 2 == 1 else range(h)

        for i in free_positions:
            t = ord(T[i]) - 97
            for c in range(t+1, 26):
                if remaining[c] > 0:
                    best_pos, best_char = i, c
                    best_snapshot = remaining[:]
                    break
            if remaining[t] > 0:
                remaining[t] -= 1
            else:
                broke = True
                break

        if not broke and n % 2 == 1:
            t = ord(T[h-1]) - 97
            if mid > t:
                best_pos, best_char = h-1, mid
                best_snapshot = remaining[:]

        candidate_b = None
        if best_pos != -1:
            prefix = T[:best_pos]
            snap = best_snapshot[:]
            snap[best_char] -= 1
            if n % 2 == 1 and best_pos == h-1:
                H = prefix + chr(best_char+97)
            else:
                rest = ''.join(chr(c+97)*snap[c] for c in range(26) if snap[c] > 0)
                if n % 2 == 1:
                    H = prefix + chr(best_char+97) + rest + chr(mid+97)
                else:
                    H = prefix + chr(best_char+97) + rest
            Hfree = H[:h-1] if n % 2 == 1 else H
            candidate_b = H + Hfree[::-1]

        if candidate_a is not None:
            return candidate_a
        if candidate_b is not None:
            return candidate_b
        return ""