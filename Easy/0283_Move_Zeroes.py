# Given an array nums, write a function to move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, count, size = 0, 0, len(nums)
        while count < size and i < size:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                i -= 1
                count += 1
            i += 1