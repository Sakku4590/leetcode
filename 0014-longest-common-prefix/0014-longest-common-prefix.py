class Solution(object):
    def longestCommonPrefix(self, words):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not words:
            return ""
    
        # Loop through the characters of the first word
        for i in range(len(words[0])):
            char = words[0][i]
            # Check if this character matches the same position in all other words
            for word in words[1:]:
                if i >= len(word) or word[i] != char:
                    return words[0][:i] # Return the prefix up to this point
                    
        return words[0]

        