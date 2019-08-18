# Given a 32-bit signed integer, reverse digits of an integer.

class Solution(object):
    def reverse(self, x):
        # Input a 32 bit signed integer
        # Output the digital reversed integer

        # Turn input integer into string
        s = str(x)
        # First object of negative numbers has to be separated to the hyphen in string from sorting
        res = int('-' + s[1:][::-1]) if s[0] == '-' else int(s[::-1])
        # For number out of range, return 0
        return res if -2147483648 <= res <= 2147483647 else 0
