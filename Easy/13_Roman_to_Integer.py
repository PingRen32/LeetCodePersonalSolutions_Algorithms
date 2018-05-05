class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Ensure all input is capitalized
        s = s.upper()
        # Create dictionary for Roman to Int
        # X = 10, L = 50, C = 100, D = 500, M = 1000
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        # Initial storage for summing up
        total = 0
        for i in range(0,len(s)-1):
            # When a smaller number is to the left of a large number means subtraction
            # The easiest way is to compare each with the one to its side
            if roman[s[i]] < roman[s[i+1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]
        # Make sure (not necessary)
        total += roman[s[-1]]
        return total
