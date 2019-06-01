# Given a string, find the length of
# the longest substring without repeating characters.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Input a charter string
        # Output the size of non-repeated longest substring

        # Empty input case
        if not s:
            return 0   
        # Initial storage for list of char, rest position and start position
        dic, res, start, = {}, 0, 0
        # Loop by all char
        for i, ch in enumerate(s):
            # If char already in dictionary
            if ch in dic:
                # Set the res updated to the larger of 'res' and length from start to current
                res = max(res, i - start)
                # Set the start updated to behind last appearance of the repeated character
                start = max(start, dic[ch] + 1)
            # Update this character into dictionary with location number
            dic[ch] = i
        # Return the larger of rest or the total length minus the starting point
        return max(res, len(s) - start)
