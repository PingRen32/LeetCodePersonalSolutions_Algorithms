class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Initialize 
        L, R, width, res = 0, len(height) - 1, len(height) - 1, 0
        # Loop by the width in reverse
        for w in range(width, 0, -1):
            # Compare the 2 items and save the larger for max 
            if height[L] < height[R]:
                res, L = max(res, height[L] * w), L + 1
            else:
                res, R = max(res, height[R] * w), R - 1
        return res