class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # Input a string of characters
        # Format into a zigzag form, start with downward then up right etc
        # Output a string in new order without blank

        # Determine the start point
        step = (numRows == 1) - 1  # 0 or -1
        # Initial string list and index
        rows, idx = [''] * numRows, 0
        # Go by each char in string
        for c in s:
            # Update string
            rows[idx] += c
            if idx == 0 or idx == numRows-1: 
                step = -step  # Change direction
            # Maintain loop
            idx += step
        return ''.join(rows)
