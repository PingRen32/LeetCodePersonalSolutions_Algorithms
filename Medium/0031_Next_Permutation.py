# Implement next permutation, which rearranges numbers into
# the lexicographically next greater permutation of numbers.
#
# If such arrangement is not possible,
# it must rearrange it as the lowest possible order
# (ie, sorted in ascending order).
#
# The replacement must be in-place and use only constant extra memory.
#
# Here are some examples.
# Inputs are in the left-hand column and
# its corresponding outputs are in the right-hand column.
#
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        index = 1
        while index < length:
            if nums[-index] <= nums[-index-1]:
                index += 1
                continue
            for i, num in enumerate(nums[::-1]):
                if num > nums[-index-1]:
                    nums[-index-1], nums[-i-1] = nums[-i-1], nums[-index-1]
                    break
            nums[:] = nums[:length-index] + nums[length-index:][::-1]
            break
        else:
            nums[:] = nums[::-1]