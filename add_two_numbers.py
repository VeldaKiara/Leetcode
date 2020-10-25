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
            
            
            