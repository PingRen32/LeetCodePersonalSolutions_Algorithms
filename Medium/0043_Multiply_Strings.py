# Given two non-negative integers num1 and num2 represented as strings,
# return the product of num1 and num2, also represented as a string.
#
# Example 1:
#
# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:
#
# Input: num1 = "123", num2 = "456"
# Output: "56088"
# Note:
#
# The length of both num1 and num2 is < 110.
# Both num1 and num2 contain only digits 0-9.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if not num1 or not num2:
            return "0"
        len1 = len(num1)
        len2 = len(num2)
        result = [0] * (len1 + len2)
        i_n1, i_n2 = 0, 0

        for i in range(len1 - 1, -1, -1):
            carry = 0
            n1 = ord(num1[i]) - 48
            i_n2 = 0
            for j in range(len2 - 1, -1, -1):
                n2 = ord(num2[j]) - 48
                summ = n1 * n2 + result[i_n1 + i_n2] + carry
                carry = summ // 10
                result[i_n1 + i_n2] = summ % 10
                i_n2 += 1
            if carry > 0:
                result[i_n1 + i_n2] += carry
            i_n1 += 1

        i = len(result) - 1
        while i >= 0 and result[i] == 0:
            i -= 1
        if i == -1:
            return "0"

        s = ""
        while i >= 0:
            s += chr(result[i] + 48)
            i -= 1
        return s