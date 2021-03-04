# Given an array nums. We define a running sum of an array as
# runningSum[i] = sum(nums[0]…nums[i]).
#
# Return the running sum of nums.

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        temp, size = 0, len(nums)

        for i in range(size):
            temp += nums[i]
            nums[i] = temp

        return nums
