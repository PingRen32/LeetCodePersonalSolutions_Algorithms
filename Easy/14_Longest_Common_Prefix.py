class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Return empty string if list is empty
        if not strs:
            return ""
        # Search for the shortest string in list as initial common prefix
        sample = min(strs,key=len)
        for i, char in enumerate(sample):
            for string in strs:
                # If a char is not the same as what is stored, its removed from sample
                if string[i] != char:
                    return sample[:i]
        return sample 
