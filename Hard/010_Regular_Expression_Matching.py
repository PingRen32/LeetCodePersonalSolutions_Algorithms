class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # Set the default result as False
        dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        # Initialize the first 
        dp[0][0] = True
        # Loop within the range of length of p and put into the first column
        for i in range(1, len(p)):
            dp[i + 1][0] = dp[i - 1][0] and p[i] == '*'
        # Loop from up to down
        for i in range(len(p)):
            # Loop from left to right
            for j in range(len(s)):
                # Judge
                if p[i] == '*':
                    dp[i + 1][j + 1] = dp[i - 1][j + 1] or dp[i][j + 1]
                    if p[i - 1] == s[j] or p[i - 1] == '.':
                        dp[i + 1][j + 1] |= dp[i + 1][j]
                else:
                    dp[i + 1][j + 1] = dp[i][j] and (p[i] == s[j] or p[i] == '.')
        return dp[-1][-1]
