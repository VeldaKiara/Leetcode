'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between
 two nodes p and q as the lowest node in T that has both p and q as descendants 
 (where we allow a node to be a descendant of itself).”

'''

class Solution:
    def __init__(self):
        #value to store the lowest common ancestor of two nodes
        self.lowest = None
        
    def lowestCommonAncestor(self, root, p, q):
        def recursiveTree(currentNode):
            #if at the end of the branch
            if not currentNode:
                return False

            #left recursive call
            left = recursiveTree(currentNode.left)

            #right recursive call
            right = recursiveTree(currentNode.right)

            #if current node is p or q
            eitherRightLeft = currentNode == p or currentNode == q

            #if either two or three var becomes true
            if eitherRightLeft + left + right >= 2:
                self.lowest = currentNode
            
            #return true if either two or three var becomes true
            return eitherRightLeft or left or right
        recursiveTree(root)
        return  self.lowest
        










