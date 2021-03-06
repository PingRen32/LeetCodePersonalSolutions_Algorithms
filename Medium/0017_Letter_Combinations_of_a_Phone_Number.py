# Given a string containing digits from 2-9 inclusive,
# return all possible letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below.
# Note that 1 does not map to any letters.

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # Input all the num pad with their according char
        map = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        # Error input
        if len(digits) == 0:
            return []
        # Using letterCombination for combining all possiable letters
        # Go from both directions
        # If the input digits can be listed
        return [a+b for a in self.letterCombinations(digits[:-1])
                    for b in self.letterCombinations(digits[-1] )] or list(map[digits])