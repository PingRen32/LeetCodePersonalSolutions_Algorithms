class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Given a array 'nums' of integers and a desired sum of two
        # aka, target = nums[a] + nums[b]
        # Find locations of a and b and return as list

        # Initiate storage hash map for O(1) backward search
        h = {}
        # Loop for each int 'num' in list 'nums'
        for i, num in enumerate(nums):
            # Check if any of int in list h could fit
            if (target - num) in h:
                # Return result
                return [i, h[target - num]]
            # Storage passed data into list in order
            h[num] = i

    # This is a O(n) since hash map won't add complexity
    # Maximum run time T(n)
