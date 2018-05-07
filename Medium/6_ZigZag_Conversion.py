class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # Determine the start point
        step = (numRows == 1) - 1  # 0 or -1
        # Initial string and index
        rows, idx = [''] * numRows, 0
        for c in s:
            # Update string
            rows[idx] += c
            if idx == 0 or idx == numRows-1: 
                step = -step  # Change direction
            # Maintain loop
            idx += step
        return ''.join(rows)
