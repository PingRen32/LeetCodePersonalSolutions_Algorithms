# You are given two non-empty linked lists representing
# two non-negative integers. The digits are stored in reverse order
# and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not
# contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode()
        if l1 and l2:
            res.val = l1.val + l2.val
            if res.val >= 10:
                res.val -= 10
                if l1.next:
                    l1.next.val += 1
                else:
                    l1.next = ListNode(1, None)
            res.next = self.addTwoNumbers(l1.next, l2.next)

        elif l1:
            res.val = l1.val
            if res.val >= 10:
                res.val -= 10
                if l1.next:
                    l1.next.val += 1
                else:
                    l1.next = ListNode(1, None)
            res.next = self.addTwoNumbers(l1.next, l2)

        elif l2:
            res.val = l2.val
            if res.val >= 10:
                res.val -= 10
                if l2.next:
                    l2.next.val += 1
                else:
                    l2.next = ListNode(1, None)
            res.next = self.addTwoNumbers(l1, l2.next)
        else:
            return None

        return res
