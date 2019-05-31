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
                n, nb = n << 1, nb << 1
        return min(result, 2147483647) if positive else max(-result, -2147483648)