# Given n non-negative integers a1, a2, ..., an ,
# where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of
# line i is at (i, ai) and (i, 0). Find two lines,
# which together with x-axis forms a container,
# such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Input a list of integer indicating lengths of bars
        # Output maximum volume(area) of water it could hold

        # Initialize boundary index and storage
        left, right, width, res = 0, len(height) - 1, len(height) - 1, 0
        # Loop by the width in reverse
        for w in range(width, 0, -1):
            # Compare the 2 items and save the larger for max
            # Only update if the volume is larger, judge for both sides
            if height[left] < height[right]:
                res, left = max(res, height[left] * w), left + 1
            else:
                res, right = max(res, height[right] * w), right - 1
        return res
