# Given an array of integers arr,
# return true if we can partition the array into three non-empty parts with equal sums.

# Formally, we can partition the array if
# we can find indexes i + 1 < j with
# (arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] ==
# arr[j] + arr[j + 1] + ... + arr[arr.length - 1])

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        s = sum(arr)

        if s % 3 != 0:
            return False

        each = s / 3
        temp, found = 0, 0

        for i in range(len(arr)):
            temp += arr[i]

            if temp == each:
                temp = 0
                found += 1

        return True if found >= 3 else False


