# Write a program that outputs the string representation of numbers from 1 to n.

# But for multiples of three it should output “Fizz” instead of the number and
# for the multiples of five output “Buzz”.
# For numbers which are multiples of both three and five output “FizzBuzz”.

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        count, res = 1, []

        while count <= n:
            if count % 3 == 0 and count % 5 == 0:
                res.append('FizzBuzz')
            elif count % 3 == 0:
                res.append('Fizz')
            elif count % 5 == 0:
                res.append('Buzz')
            else:
                res.append(str(count))
            count += 1
        return res
