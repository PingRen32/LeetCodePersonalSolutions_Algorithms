# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Seperate the unchanged from input
        pre, pre.next = self, head
        # When there are still more than two nodes left
        while pre.next and pre.next.next:
            # Save the nodes from pre,a,b,b.next to pre,b,a,b.next
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next