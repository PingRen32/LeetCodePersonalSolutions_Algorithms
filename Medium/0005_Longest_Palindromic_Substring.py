# Given a string s, find the longest palindromic substring in s.
# You may assume that the maximum length of s is 1000.

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Input a string 's'
        # Output the longest palindromic substring

        # Transform 's' into t
        # For example, S = "abba", t = "^#a#b#b#a#$"
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        t = '#'.join('^{}$'.format(s))
        # Length of t
        n = len(t)
        # List of boolean (also int) same length as t
        p = [0] * n
        # Place holders
        c = r = 0
        for i in range(1, n-1):
            # Equals to i' = c - (i-c)
            p[i] = (r > i) and min(r - i, p[2*c - i])
            # Attempt to expand palindrome centered at i
            while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
                p[i] += 1
            # If palindrome centered at i expand past r,
            # adjust center based on expanded palindrome.
            if i + p[i] > r:
                c, r = i, i + p[i]
    
        # Find the maximum element in p.
        max_len, center_index = max((n, i) for i, n in enumerate(p))
        # Return the value by having midpoint expand to both sides
        return s[(center_index - max_len)//2: (center_index + max_len)//2]
