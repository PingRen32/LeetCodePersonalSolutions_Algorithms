# You are given a string, s, and a list of words, words, that are all of the same length.
# Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once
# and without any intervening characters.
#
# Example 1:
#
# Input:
#   s = "barfoothefoobarman",
#   words = ["foo","bar"]
# Output: [0,9]
#
# Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
# The output order does not matter, returning [9,0] is fine too.
# Example 2:
#
# Input:
#   s = "wordgoodgoodgoodbestword",
#   words = ["word","good","best","word"]
# Output: []

# You are given a string, s, and a list of words, words, that are all of the same length.
# Find all starting indices of substring(s) in s that is a concatenation
# of each word in words exactly once and without any intervening characters.

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # Empty string
        if len(words) is 0:
            return []
        # Separate individual character from words
        storage = {}
        for char in words:
            storage[char] = storage.get(char, 0) + 1
        # Log length of first word, total number of words and total length
        word = len(words[0])
        num = len(words)
        total = word * num
        string = len(s)
        i = 0
        result = []
        while i <= string - total:
            bgn = i
            end = i + total
            used = {}
            while i < end:
                temp = s[i:i + word]
                if temp not in storage:
                    break
                used[temp] = used.get(temp, 0) + 1
                if used[temp] > storage[temp]:
                    break
                i += word
            if i == end:
                result.append(bgn)
            i = bgn + 1
        return result