# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Return the other ListNode if one is empty
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        # Initial the condistions
        head = ListNode(None)
        merge = head
        # Start comparison
        while l1 != None and l2 != None:
            # Storage the larger value to the tail
            if l1.val > l2.val:
                merge.next = l2
                l2 = l2.next
                merge = merge.next
            else:
                merge.next = l1
                l1 = l1.next
                merge = merge.next
        # End the process when one of them is empty, with the rest linked behind
        if l2 == None:
            merge.next = l1
            return head.next
        else:
            merge.next = l2
            return head.next
