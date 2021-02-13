# Given a string, determine if it is a palindrome,
# considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, 
# we define empty string as valid palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = []
        for c in s:
            if c.isalnum():
                temp.append(c.upper())

        if temp == temp[::-1]:
            return True
        else:
            return False