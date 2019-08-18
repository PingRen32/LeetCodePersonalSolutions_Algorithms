# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Remove the characters by pairs
        for i in range(0,len(s)):
            s = s.replace('()', '')
            s = s.replace('[]', '')
            s = s.replace('{}', '')
        # Element remains in the string
        if len(s)!=0:
            return False
        else: 
            return True
