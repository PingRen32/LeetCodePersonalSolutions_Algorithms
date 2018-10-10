class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Initiate
        h = {}
        # Loop for each int in list
        for i, num in enumerate(nums):
            # Check if any of int in list h could fit
            if (target - num) in h:
                # Return result
                return [i, h[target - num]]
            # Storage passed data into list
            h[num] = i
