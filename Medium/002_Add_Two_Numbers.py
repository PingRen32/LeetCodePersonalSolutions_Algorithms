# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Input two linked nodes 'l1' and 'l2' each defined ahead on top
        # Sum each according to single digit result by pushing tenth digit '1' of two digit results to next node

        # Start with first item of list node
        dummy = cur = ListNode(0)
        # Carry current sum of two list nodes
        carry = 0
        # When node item still exists
        while l1 or l2 or carry:
            # Two conditions, in case one of them already ended
            if l1:
                # Pass value to sum
                carry += l1.val
                # Update toward next node
                l1 = l1.next
            if l2:
                # Pass value to sum
                carry += l2.val
                # Update toward next node
                l2 = l2.next
            # Add last digit of sum
            cur.next = ListNode(carry%10)
            # Update node
            cur = cur.next
            # Adding remainder toward next
            carry //= 10
        return dummy.next
