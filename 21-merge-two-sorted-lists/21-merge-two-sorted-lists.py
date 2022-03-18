# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #create a dummy node, to avoid the edge case of using an empty list
        dummy = ListNode()
        tail = dummy
        
        #iterate through the list, if both of them are non empty
        while list1 and list2:
            if list1.val < list2.val:
                #insert the value to the tail
                tail.next = list1
                #update list one pointer
                list1 = list1.next
            else:
                #insert it in list 2
                tail.next = list2
                list2 = list2.next
                
            #update the tail pointer regardless
            tail = tail.next
            
            #incase one of the lists is empty and the other is not
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next
    
            
        
        
        
        