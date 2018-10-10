class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Remove the characters by pairs
        for i in range(0,len(s)):
            s = s.replace('()','')
            s = s.replace('[]','')
            s = s.replace('{}','')
        # Element remains in the string
        if len(s)!=0:
            return False
        else: 
            return True
