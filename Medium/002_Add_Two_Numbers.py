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
        dummy = cur = ListNode(0)
        carry = 0
        # When node still exists
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
