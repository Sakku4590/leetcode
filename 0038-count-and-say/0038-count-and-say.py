class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = "1"

        for _ in range(n - 1):
            new_string = ""
            count = 1

            for i in range(1, len(result)):
                if result[i] == result[i - 1]:
                    count += 1
                else:
                    new_string += str(count) + result[i - 1]
                    count = 1

            # Add the last group
            new_string += str(count) + result[-1]

            result = new_string

        return result
        