'''You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Constraints:
-The number of nodes in each linked list is in the range [1, 100].
-The0 <= Node.val <= 9
-It is guaranteed that the list represents a number that does not have leading zeros.
'''


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dope = ListNode(0)
        l3 = dope
        
        carry = 0
        while l1 != None and l2 != None:
            value = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry ) // 10
            
            l3.next = ListNode(value)
            l3 = l3.next
            
            l1 = l1.next
            l2 = l2.next
            
        while l1 != None:
            value = (l1.val + carry) %10
            carry = (l1.val + carry) // 10
            
            l3.next = ListNode(value)
            l3 = l3.next
            l1 = l1.next
            
        while l2 != None:
            value = (l2.val + carry) %10
            carry = (l2.val + carry) // 10
            
            l3.next = ListNode(value)
            l3 = l3.next
            l2 = l2.next
        
        if carry != 0:
            l3.next = ListNode(carry)
        
        return dope.next
            
            
            