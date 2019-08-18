class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Null input case
        if not nums:
            return 0
        # Initial variables
        cur_sum = max_sum = nums[0]
        for num in nums[1:]:
            # If sum toward current number is not lager than the max item already exits
            # the current sum will be stored as current single value
            cur_sum = max(num, cur_sum + num)
            # Update the max sum
            max_sum = max(max_sum, cur_sum)
        return max_sum            
