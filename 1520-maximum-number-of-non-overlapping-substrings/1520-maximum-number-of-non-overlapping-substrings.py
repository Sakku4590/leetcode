class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        candidates = []
        for i in range(n):
            ch = s[i]
            if first[ch] != i:
                continue  # only first-occurrence positions can start a valid substring

            end = last[ch]
            j = i
            valid = True
            while j <= end:
                c = s[j]
                if first[c] < i:
                    valid = False
                    break
                if last[c] > end:
                    end = last[c]
                j += 1

            if valid:
                candidates.append((i, end))

        # Greedy: sort by end, pick earliest-finishing non-overlapping intervals
        candidates.sort(key=lambda x: (x[1], x[0]))

        result = []
        last_end = -1
        for start, end in candidates:
            if start > last_end:
                result.append(s[start:end + 1])
                last_end = end

        return result