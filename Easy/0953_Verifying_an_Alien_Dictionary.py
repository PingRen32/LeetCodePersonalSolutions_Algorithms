# In an alien language, surprisingly they also use english lowercase letters,
# but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
#
# Given a sequence of words written in the alien language, and the order of the alphabet,
# return true if and only if the given words are sorted lexicographicaly in this alien language.

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words)-1):
            ind = 0
            while True:
                if ind < len(words[i]) and ind < len(words[i+1]):
                    if order.index(words[i][ind]) > order.index(words[i+1][ind]):
                        return False
                    elif order.index(words[i][ind]) < order.index(words[i+1][ind]):
                        break
                elif len(words[i]) > len(words[i+1]):
                    return False
                else:
                    break
                ind += 1
        return True









