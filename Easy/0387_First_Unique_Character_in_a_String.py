# Given a string, find the first non-repeating character in it and return its index.
# If it doesn't exist, return -1.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        temp = {}

        for i in range(len(s)):
            if s[i] not in temp:
                temp[s[i]] = 1
            else:
                temp[s[i]] += 1

        for c, count in temp.items():
            if count == 1:
                return s.index(c)

        return -1
