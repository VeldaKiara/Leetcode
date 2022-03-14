# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#time O(n) 
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int):
        '''
        n is the value to remove from  starting from the end 
        add a dummy, use two pointers maintain n as the distance between
        the two values,
        remove the value and update the next values
        return dummy.next because  we do not want the dummy data
        '''
        #create a dummy
        dummy = ListNode(0, head)
        left = dummy
        right = head 
        
        #while n is not zero and right is not none
        while n > 0 and right is not None:
            #shift right
            right = right.next
            #when n is zero we have shifted with value of n, decrement n
            n -= 1
            
        #shift left and right 
        while right is not None:
            left = left.next
            right = right.next
            
        
        #delete the node, by updating left pointer
        left.next = left.next.next
        return dummy.next

            
            

            