# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # Seperate generation for each possibility
        def generate(p, left, right):
            # Keep looping if not closed(well-formed)
            if right >= left >= 0:
                # Complete checking
                if not right:
                    yield p
                # Add one parenthese at a time, pile up for final result
                for q in generate(p + '(', left-1, right): yield q
                for q in generate(p + ')', left, right-1): yield q
        return list(generate('', n, n))
