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
