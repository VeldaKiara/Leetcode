# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#l, r , sum 
'''
root1 node + root2 node 
left root 1 + left root 2
 while root1:
            v = root1.val + root2.val
            left_val
 base case if empty           

'''
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 == None:
            return  root2
        if root2 == None:
            return root1
        if  not root1 and not root2:
            return None
        # if not root2:
        #     return None
        #create root3
        root3 = TreeNode(root1.val + root2.val)
        root3.left = self.mergeTrees(root1.left, root2.left)
        root3.right = self.mergeTrees(root1.right, root2.right)
        return root3
        
        
        
            
            
            
            
            
    
        
        
        