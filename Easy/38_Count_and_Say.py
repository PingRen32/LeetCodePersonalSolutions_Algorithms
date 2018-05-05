class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # Single item case
        if n == 1: return "1"
        # Recursion with current n times
        s = self.countAndSay(n-1)
        # Initial position count, first character, and new string storage
        i, ch, tmp = 0, s[0], ''
        for j in range(1, len(s)):
            # If the value returned object starts with "11"
            if s[j] != ch:
                tmp += str(j-i) + ch
                # Update with next item
                i, ch = j, s[j]
        # Add last value to return
        tmp += str(len(s)-i) + ch
        return tmp
