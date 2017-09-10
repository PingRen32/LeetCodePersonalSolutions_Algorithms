class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(0,len(s)):
            s = s.replace('()','')
            s = s.replace('[]','')
            s = s.replace('{}','')
        if len(s)!=0:
            return False
        else: 
            return True
