class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Initialize Roman characters to numbers
        strs = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]        
        # Initialize Storage for result
        ret = ""
        # Loop with the Roman number table from largest to smallest
        for i, j in enumerate(nums):
            # When the number input is larger than the one compared
            while num >= j:
                # Pass the character to the result 
                ret += strs[i]
                # Remove according number from the input number
                num -= j
                # End when there is no nuber left
            if num == 0:
                return ret