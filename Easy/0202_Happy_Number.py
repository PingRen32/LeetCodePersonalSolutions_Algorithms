# Write an algorithm to determine if a number n is happy.
#
# A happy number is a number defined by the following process:
#
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay),
# or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
#
# Return true if n is a happy number, and false if not.

class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 0:
            return False

        for i in range(6):
            n = self.check(n)

        if n == 1:
            return True
        return False

    def check(self, i: int) -> int:
        res = 0

        while i > 0:
            res += (i % 10) ** 2
            i = i // 10

        return res

