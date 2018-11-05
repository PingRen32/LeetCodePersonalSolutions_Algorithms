class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Input a integer number
        # Output a string of Roman number

        # Initialize Roman characters to numbers dictionary
        strs = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]        
        # Initialize Storage for result
        ret = ""
        # Since the Roman numeral proceed by reading digit from left to right
        # Loop with the Roman number table from largest to smallest and subtract any already transformed
        for i, j in enumerate(nums):
            # When the number input is larger than the one compared
            while num >= j:
                # Pass the character to the result 
                ret += strs[i]
                # Remove according number from the input number
                num -= j
                # End when there is no number left
            if num == 0:
                # When number is 0, return the string
                return ret
