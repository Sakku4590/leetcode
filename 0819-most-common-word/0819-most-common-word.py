class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = paragraph.lower()
        cleaned = re.sub(r"[!?.,;']", " ", paragraph)
        words = cleaned.split()

        dic = {}
        for ch in words:
            if ch not in banned:
                dic[ch] = dic.get(ch, 0) + 1
        most_frequent = max(dic, key=dic.get)
        return most_frequent
        