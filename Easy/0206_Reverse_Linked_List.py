# Reverse a singly linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        temp, node = [], head
        while node != None:
            temp.append(node.val)
            node = node.next

        node, dim = head, len(temp)
        for i in range(dim):
            node.val = temp[dim - i - 1]
            node = node.next

        return head

