class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        # Universal solver for summery questions
        def ksum(num, k, target):
            i = 0
            # Sum of 2
            if k == 2:
                j = len(num) - 1
                while i < j:
                    if num[i] + num[j] == target:
                        yield (num[i], num[j])
                        i += 1
                    elif num[i] + num[j] > target:
                        j -= 1
                    else:
                        i += 1
            # Sum of more (k)
            else:
                while i < len(num) - k + 1:
                    newtarget = target - num[i]
                    for sub in ksum(num[i + 1:], k - 1, newtarget):
                        yield (num[i],) + sub
                    i += 1
        return [list(t) for t in set(ksum(nums, 4, target))]
