# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = jump = ListNode(0)
        dummy.next = l = r = head

        while True:
            count = 0
            while r and count < k:
                # locate last node in range
                r = r.next
                count += 1
            # When reaching the end for reversing, reverse backward toward head
            if count == k:
                # 3 node needed for reversing each node, the one before and after target node
                pre, cur = r, l
                for _ in range(k):
                    # Reverse all node
                    cur.next, cur, pre = pre, cur.next, cur
                    # Connect two k-groups
                jump.next, jump, l = pre, l, r
            else:
                return dummy.next
