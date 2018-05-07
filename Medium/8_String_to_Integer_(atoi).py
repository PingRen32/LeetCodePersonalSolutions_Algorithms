class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # If empty input
        if len(str) == 0:
            return 0
        # Turn string into list
        ls = list(str.strip())
        # Initialize sign by judging the first char
        sign = -1 if ls[0] == '-' else 1
        # Remove sign symbols
        if ls[0] in ['-', '+']:
            del ls[0]
        # Initialize 2 int
        ret, i = 0, 0
        # Loop within length of list while list item is still digit
        while i < len(ls) and ls[i].isdigit():
            # Using ord to turn anything not digit into digit and store into ret
            ret = ret*10 + ord(ls[i]) - ord('0')
            # Looping
            i += 1
        # Return the result if in range, by max with min and min to max
        return max(-2**31, min(sign * ret, 2**31-1))
