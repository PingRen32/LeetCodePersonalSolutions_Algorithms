# Given an array nums and a value val,
# remove all instances of that value in-place and return the new length.
#
# Do not allocate extra space for another array,
# you must do this by modifying the input array in-place with O(1) extra memory.
#
# The order of elements can be changed.
# It doesn't matter what you leave beyond the new length.

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        try:
            # Continuously remove specific val until all removed
            while True:
                nums.remove(val)
        except:
            # Return length left
            return len(nums)
