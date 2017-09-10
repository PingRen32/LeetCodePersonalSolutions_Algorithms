class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x >= 0:
            if x<=9:
                return True
            else:
                s = str(x)
                res = int(s[::-1])
                return True if res==x else False
        else:
            return False