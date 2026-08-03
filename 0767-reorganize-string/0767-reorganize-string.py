class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = Counter(s)
        n = len(s)

        # Impossible case
        if max(freq.values()) > (n + 1) // 2:
            return ""

        # Max heap (Python has min heap, so use negative frequencies)
        heap = [(-count, ch) for ch, count in freq.items()]
        heapq.heapify(heap)

        result = []

        prev_count = 0
        prev_char = ""

        while heap:
            count, ch = heapq.heappop(heap)

            result.append(ch)

            # count is negative, so +1 reduces its absolute frequency
            count += 1

            # Push back the previous character if it still has remaining count
            if prev_count < 0:
                heapq.heappush(heap, (prev_count, prev_char))

            # Store current character for the next iteration
            prev_count = count
            prev_char = ch

        return "".join(result)
        