"""
STATEMENT
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

EXAMPLES
(2 -> 4 -> 3), (5 -> 6 -> 4) -> 7 -> 0 -> 8
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def addTwoNumbers(self, l1, l2):
        new = ListNode(0)
        answer = new
        carry = 0
        
        while l1 is not None and l2 is not None:
            new.next = ListNode(0)
            new = new.next
            sum_val = carry + l1.val + l2.val
            rem = sum_val%10
            new.val  = rem
            if sum_val>9:
                carry = 1
            else:
                carry = 0

            l1 = l1.next
            l2 = l2.next
        
        
        while l1 is not None:
            new.next = ListNode(0)
            new = new.next
            sum_val = carry + l1.val
            rem = sum_val%10
            new.val  = rem
            if sum_val>9:
                carry = 1
            else:
                carry = 0

            l1 = l1.next

        while l2 is not None:
            new.next = ListNode(0)
            new = new.next
            sum_val = carry + l2.val
            rem = sum_val%10
            new.val  = rem
            if sum_val>9:
                carry = 1
            else:
                carry = 0

            l2 = l2.next
        
        if carry == 1:
            new.next = ListNode(carry)
        
        return answer.next