class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        n=len(nums)
        count=curr=1
        while count < n:
            if nums[curr]!=nums[curr-1]:
                curr+=1
            else:
                del nums[curr]
            count+=1
        return curr