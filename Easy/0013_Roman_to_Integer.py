# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# For example, two is written as II in Roman numeral,
# just two one's added together.
# Twelve is written as, XII, which is simply X + II.
# The number twenty seven is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII.
# Instead, the number four is written as IV.
# Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX.
# There are six instances where subtraction is used:
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.
# Input is guaranteed to be within the range from 1 to 3999.

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Input a string of Roman number
        # Output a integer number

        # Ensure all input is capitalized
        s = s.upper()
        # Create dictionary for Roman to Int
        # I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000
        roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        # Initial storage for summing up integer
        total = 0
        for i in range(0, len(s)-1):
            # When a smaller number is to the left of a large number means subtraction
            # The easiest way is to compare each with the one to its side
            if roman[s[i]] < roman[s[i+1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]
        # Make sure (not necessary)
        total += roman[s[-1]]
        return total
