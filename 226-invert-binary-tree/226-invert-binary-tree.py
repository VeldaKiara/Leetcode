# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

''' 
recursive approach
#o(n) time / o(d) space, d for depth
'''
class Solution:
    def invertTree(self, root):
        if root is None:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
    
        
        
        
        
        