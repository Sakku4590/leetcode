class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:
            # Opening bracket
            if ch in "([{":
                stack.append(ch)
            else:
                # No opening bracket to match
                if not stack:
                    return False

                # Top of the stack must match
                if stack[-1] == pairs[ch]:
                    stack.pop()
                else:
                    return False

        # Stack should be empty if all brackets matched
        return len(stack) == 0
        