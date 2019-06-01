# Given a sorted array nums, remove the duplicates in-place such
# that each element appear only once and return the new length.
#
# Do not allocate extra space for another array,
# you must do this by modifying the input array in-place with O(1) extra memory.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Return empty list as it was
        if not nums:
            return 0
        # Get length and start counting
        n = len(nums)
        count = curr = 1
        while count < n:
            # If not occurred, the number is ignored
            if nums[curr] != nums[curr-1]:
                curr += 1
            else:
                # Remove duplicate number
                del nums[curr]
            count += 1
        return curr
