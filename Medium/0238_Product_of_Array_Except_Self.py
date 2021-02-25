# Given an array nums of n integers where n > 1,
# return an array output such that output[i] is equal to the product of
# all the elements of nums except nums[i].
#
# Constraint: It's guaranteed that the product of the elements of
# any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.
#
# Note: Please solve it without division and in O(n).
#
# Follow up:
# Could you solve it with constant space complexity?
# (The output array does not count as extra space for the purpose of space complexity analysis.)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        for i in range(1, len(nums)):
            result[i] = nums[i - 1] * result[i - 1]

        right_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= right_prod
            right_prod *= nums[i]

        return result
