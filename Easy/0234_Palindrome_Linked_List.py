# Given a singly linked list, determine if it is a palindrome.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        temp = []
        while head != None:
            temp.append(head.val)
            head = head.next

        if temp == temp[::-1]:
            return True
        else:
            return False
