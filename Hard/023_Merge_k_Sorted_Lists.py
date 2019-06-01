# Merge k sorted linked lists and return it as one sorted list.
# Analyze and describe its complexity.
#
# Example:
#
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from heapq import heappush, heappop, heapreplace, heapify
        # Initialize lists
        dummy = node = ListNode(0)
        # Turn list into heap
        h = [(n.val, n) for n in lists if n]
        heapify(h)
        # While h is not empty
        while h:
            # Extract first value and node number
            v, n = h[0]
            if n.next is None:
                # The end of the lists
                heappop(h)
            else:
                # Remove used nodes
                heapreplace(h, (n.next.val, n.next))
            # Save node to list
            node.next = n
            node = node.next

        return dummy.next