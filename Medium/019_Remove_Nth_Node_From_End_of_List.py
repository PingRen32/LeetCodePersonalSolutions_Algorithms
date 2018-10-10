# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # Recursion method
        def remove(head):
            # Input Error Report
            if not head:
                return 0, head
            i, head.next = remove(head.next)
            # Start with i and remove each one that is on the n th point
            return i+1, (head, head.next)[i+1 == n]
        return remove(head)[1]
