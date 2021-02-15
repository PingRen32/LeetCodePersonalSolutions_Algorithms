# Given a non-empty string s, you may delete at most one character.
# Judge whether you can make it a palindrome.

class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        else:
            ind, temp = 0, s[::-1]
            for i in range(len(s)):
                if s[i] != temp[i]:
                    ind = i
                    break
            temp = temp[:ind] + temp[ind+1:]
            if temp == temp[::-1]:
                return True
            temp = s[:ind] + s[ind+1:]
            if temp == temp[::-1]:
                return True
        return False