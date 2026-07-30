class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        counts = Counter(s)

        result = [char * count for char, count in counts.most_common()]

        return "".join(result)
        