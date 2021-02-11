# Given two non-negative integers num1 and num2 represented as string,
# return the sum of num1 and num2.

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ind, add, res, dim1, dim2 = 0, 0, "", len(num1), len(num2)

        while True:
            if ind < dim1 and ind < dim2:
                val = int(num1[dim1-ind-1]) + int(num2[dim2-ind-1]) + add
                res += str(val % 10)
                add = val // 10
            elif ind < dim1:
                val = int(num1[dim1-ind-1]) + add
                res += str(val % 10)
                add = val // 10
            elif ind < dim2:
                val = int(num2[dim2-ind-1]) + add
                res += str(val % 10)
                add = val // 10
            elif add == 1:
                res += "1"
                add = 0
            else:
                break
            ind += 1
        return res[::-1]
