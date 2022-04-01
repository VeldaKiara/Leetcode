# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]):
        #handling edge cases if list is null or len(0)
        if not lists or len(lists) == 0:
            return None
        #pairing the linked lists and merging them each time
        while len(lists) > 1:
            mergedLists = [ ]
            #iterate till we get the one list 
            for i in range(0, len(lists), 2):
                firstList = lists[ i ]
                #check if list is in bound
                secondList = lists[i + 1] if (i + 1) < len(lists) else None
                #helper func
                mergedLists.append(self.mergeKListsHelper(firstList, secondList))
            lists = mergedLists       
        return lists[0]
    
    def mergeKListsHelper(self, firstList, secondList):
        dummy = ListNode()
        tail = dummy
        while firstList and  secondList:
            if firstList.val < secondList.val:
                tail.next = firstList
                firstList = firstList.next
            else:
                tail.next = secondList
                secondList = secondList.next
            tail  = tail.next
            
        if firstList:
            tail.next = firstList
        if secondList:
            tail.next = secondList
        return dummy.next
            
                
                 
                    
                    
                
                
        
        