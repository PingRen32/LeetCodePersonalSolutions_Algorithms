# Given a string containing just the characters '(' and ')',
# find the length of the longest valid (well-formed) parentheses substring.
#
# Example 1:
#
# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
# Example 2:
#
# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Stack for storage and longest as counter
        stack, longest = [0], 0
        for pos, c in enumerate(s):
            if c == '(':
                stack.append(pos + 1)
            elif stack.pop() > 0:
                # If last char is ( while current char is )
                longest = max(longest, pos + 1 - abs(stack[-1]))
            else:
                stack.append(-pos - 1)
        return longest