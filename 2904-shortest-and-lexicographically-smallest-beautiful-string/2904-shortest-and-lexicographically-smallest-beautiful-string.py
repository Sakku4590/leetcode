class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        answer = ""

        for left in range(n):
            ones = 0

            for right in range(left, n):
                if s[right] == '1':
                    ones += 1

                if ones == k:
                    current = s[left:right + 1]

                    if (answer == "" or
                        len(current) < len(answer) or
                        (len(current) == len(answer) and current < answer)):
                        answer = current

                    # Adding more characters can only make
                    # the substring longer, so stop.
                    break

                if ones > k:
                    break

        return answer