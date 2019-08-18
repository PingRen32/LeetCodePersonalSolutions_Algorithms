class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """        
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        # Target is the largest
        return len(nums)
