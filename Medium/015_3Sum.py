# Given an array nums of n integers,
# are there elements a, b, c in nums such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.
#
# Note:
# The solution set must not contain duplicate triplets.

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Input a list of integer
        # Output a list of integer lists that sum up to 0

        # Initialize result string
        res = []
        # Sort the given numbers
        nums.sort()
        for i in range(len(nums)-2):
            # If two numbers are same, the sum must be non zero therefore keep going
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # search for reuslt from the current item to the end from both ends
            l, r = i+1, len(nums)-1
            # All the items are checked if l =< r
            while l < r:
                # Sum the three items
                s = nums[i] + nums[l] + nums[r]
                # If the sum too small, move the first item backward aka a larger one 
                if s < 0:
                    l +=1 
                # If the sum too big, move the second moving item forward for smaller one
                elif s > 0:
                    r -= 1
                else:
                    # When the sum is zero, push the result string to the main result string
                    res.append((nums[i], nums[l], nums[r]))
                    # For the same items, save to result directly
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    # Same as the one above
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    # move l forward and r backward (actrually 2 cases above is not necessary)
                    l += 1; r -= 1
        # Return the result
        return res
