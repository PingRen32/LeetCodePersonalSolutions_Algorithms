class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # If the string split into length 0, meaning input is null or all blank
        # Return the length item of the list of split items
        return 0 if len(s.split()) == 0 else len(s.split()[-1])
