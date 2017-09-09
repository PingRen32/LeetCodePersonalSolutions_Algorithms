class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        sample = min(strs,key=len)
        for i, char in enumerate(sample):
            for string in strs:
                if string[i] != char:
                    return sample[:i]
        return sample 