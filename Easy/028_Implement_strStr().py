# Implement strStr().
#
# Return the index of the first occurrence of needle in haystack,
# or -1 if needle is not part of haystack.
#
# Example 1:
#
# Input: haystack = "hello", needle = "ll"
# Output: 2
#
# Example 2:
#
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1

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
