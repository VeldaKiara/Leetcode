# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
one idea would be to use a hashset, have the values of list a then compare the values with b
if the value at b and a match, them that is the intersection
this involves using memory which is 
if they do not intersect no similar values return null
set the head of both lists 
increment while both of them are not equal, if none of them are null

you can return either number, when they are equal


'''

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        list_one, list_two = headA, headB
        while list_one != list_two:
            list_one = list_one.next if list_one else headB
            list_two = list_two.next if list_two else headA
        return list_one 
            
            
        