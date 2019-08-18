# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Input a list of strings
        # Output the longest common prefix

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
