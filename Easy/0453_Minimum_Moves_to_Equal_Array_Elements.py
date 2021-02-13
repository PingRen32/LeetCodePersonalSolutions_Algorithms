# Given a non-empty integer array of size n,
# find the minimum number of moves required to make all array elements equal,
# where a move is incrementing n - 1 elements by 1.

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - min(nums) * len(nums)
