class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Empty needle
        if not needle:
            return 0
        # Empty haystack
        elif not haystack:
            return -1
        # Search for location
        location = haystack.find(needle)
        return location
