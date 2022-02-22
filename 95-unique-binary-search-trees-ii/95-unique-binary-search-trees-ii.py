'''
step 1: create a func to return all valid bst where values are in the range of left & right
step 2 the result will be the func(1,n)
step 3:Func deets; generate root from the range of values between right and left
get left subtrees by calling func on the left, and using root -1, get right subtrees by calling func root+1, right.
combine the left nodes and right nodes to form trees
Step 4:cache the result to prevent recomputing multiple times
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
         
class Solution:
    def generateTrees(self, n):
        @lru_cache(None)
        def dfs(left, right):
            if left > right: 
                return [None]
            if left == right: 
                return [TreeNode(left)]
            treeList = []
            for root in range(left, right+1):
                leftNodes = dfs(left, root - 1)
                rightNodes = dfs(root+1, right)
                for leftNode in leftNodes:
                    for rightNode in rightNodes:
                        rootNode = TreeNode(root, leftNode, rightNode)
                        treeList.append(rootNode)
            return treeList
        
        return dfs(1, n)
        
        