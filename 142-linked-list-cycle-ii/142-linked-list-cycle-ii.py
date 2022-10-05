# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
null if no cycle, -1
cycle values have seen before
pointers, next val

store = [ ]
add point 3 to store
 4 
 p
'''
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return    
        captain, falcon = head, head 
        while captain and captain.next:
            captain = captain.next.next 
            falcon = falcon.next
            if captain == falcon:
                break
        else:
            return None
        captain = head
        while captain != falcon:
            captain = captain.next
            falcon = falcon.next         
            
        return captain 
            
            
            
            

        
        
        
        
        
        
        
        
        
        
        
        
        