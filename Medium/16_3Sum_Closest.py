class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Sort the given numbers
        nums.sort()
        # Initialize result
        res = nums[0]+nums[1]+nums[2]
        if res == target:
            return target
        
        for i in range(len(nums)-2):
            # search for reuslt from the current item to the end from both ends
            j, k = i+1, len(nums)-1
            # All the items are checked if l =< r
            while j < k:
                # Sum the three items
                s = nums[i] + nums[j] + nums[k]
                # Return result if there is a target result 
                if s == target:
                    return target
                # Update result with closet
                if abs(s-target)<abs(res-target):
                    res = s
                if s < target:
                    j += 1
                elif s > target:
                    k -= 1
        # Return the result
        return res