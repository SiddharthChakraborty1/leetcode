"""You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.

The digits are stored in reverse order, e.g. the number 321 is represented as 1 -> 2 -> 3 -> in the linked list.

Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Return the sum of the two numbers as a linked list."""


from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = l1
        h2 = l2
        dummy = ListNode(0)
        current = dummy
        remainder = 0
        while h1 or h2 or remainder:
            total = 0
            if h1: total += h1.val
            if h2: total += h2.val
            total += remainder
            remainder = total// 10
        
            current.next = ListNode(total % 10)
            current = current.next
            if h1: h1 = h1.next
            if h2: h2 = h2.next
        
        return dummy.next
