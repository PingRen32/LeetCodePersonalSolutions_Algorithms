# Given two binary strings, return their sum (also a binary string).
# #
# # The input strings are both non-empty and contains only characters 1 or 0.
# #
# # Example 1:
# #
# # Input: a = "11", b = "1"
# # Output: "100"
# # Example 2:
# #
# # Input: a = "1010", b = "1011"
# # Output: "10101"

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        added = list(map(int, str(int(a) + int(b))))
        increment, res = 0, []
        while added:
            digit = added.pop() + increment
            if digit < 2:
                res.append(digit)
                increment = 0
            else:
                res.append(digit - 2)
                increment = 1
        if increment == 1:
            res.append(1)
        res.reverse()
        return "".join([str(i) for i in res.reverse()])