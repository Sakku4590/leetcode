class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cur = [0] * 26
        for ch in s:
            cur[ord(ch) - 97] += 1

        best_i = -1
        best_remaining = None
        best_char = None

        for i in range(n):
            t = ord(target[i]) - 97

            # Check if we can diverge here with a char > target[i]
            for c in range(t + 1, 26):
                if cur[c] > 0:
                    best_i = i
                    best_remaining = cur[:]
                    best_char = c
                    break  # smallest such c found, since we scan ascending

            # Try to continue matching target[i] exactly
            if cur[t] == 0:
                break
            cur[t] -= 1

        if best_i == -1:
            return ""

        best_remaining[best_char] -= 1
        rest_chars = []
        for c in range(26):
            if best_remaining[c]:
                rest_chars.append(chr(c + 97) * best_remaining[c])
        rest = ''.join(rest_chars)

        return target[:best_i] + chr(best_char + 97) + rest