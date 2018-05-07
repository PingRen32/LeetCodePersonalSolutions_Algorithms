class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Empty input case
        if not s:
            return 0   
        # Initial storage for list of char, rest position and start position
        dic, res, start, = {}, 0, 0
        # Loop by all char
        for i, ch in enumerate(s):
            if ch in dic:
                # If char already in dictionary
                # Set the length to be ended by current location
                res = max(res, i - start)
                # Update to the location of next item on char list
                # Abandoning the repeated char
                start = max(start, dic[ch] + 1)
            # Update location for that char
            dic[ch] = i
        return max(res, len(s) - start)
