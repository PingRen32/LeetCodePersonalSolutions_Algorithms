# Given two integers dividend and divisor, divide two integers without using multiplication,
# division and mod operator.
#
# Return the quotient after dividing dividend by divisor.
#
# The integer division should truncate toward zero.
#
# Example 1:
#
# Input: dividend = 10, divisor = 3
# Output: 3
#
# Example 2:
#
# Input: dividend = 7, divisor = -3
# Output: -2
# Note:
#
# Both dividend and divisor will be 32-bit signed integers.
# The divisor will never be 0.
# Assume we are dealing with an environment which could only store integers within
# the 32-bit signed integer range: [−2**31,  2**31 − 1].
# For the purpose of this problem, assume that your function returns 2**31 − 1
# when the division result overflows.

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive, dividend, divisor, result = (dividend >= 0) ^ (divisor < 0), abs(dividend), abs(divisor), 0
        while dividend >= divisor:
            n, nb = 1, divisor
            while dividend >= nb:
                dividend, result = dividend - nb, result + n
                # Update by bit for both update factor and result addition
                # Adding 1, 2, 4, 8 toward result with updated divisor
                n, nb = n << 1, nb << 1
        return min(result, 2147483647) if positive else max(-result, -2147483648)