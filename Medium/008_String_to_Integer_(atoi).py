class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # Input a string
        # Output a 32 bit integer number from the given string
        # convert only when string is started with +/- or number, whitespace ignored

        # If empty input
        if len(str) == 0:
            return 0

        # Turn string into list
        ls = list(str.strip())
        # Initialize sign by judging the first char
        sign = -1 if ls[0] == '-' else 1
        # Remove sign symbols from list
        if ls[0] in ['-', '+']:
            del ls[0]
        # Initialize storage and counter
        ret, i = 0, 0
        # Loop within length of list while list item is still digit
        # If there is a char in middle, terminate the process
        while i < len(ls) and ls[i].isdigit():
            # Using ord to turn anything not digit into digit and store into result
            ret = ret*10 + ord(ls[i]) - ord('0')
            # Looping
            i += 1
        # Return the result within 32 bit range
        return max(-2**31, min(sign * ret, 2**31-1))
