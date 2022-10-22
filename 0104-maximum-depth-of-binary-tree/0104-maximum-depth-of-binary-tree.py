# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #DFs, recursive, left + right
        if not root:
            return 0
        
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        # def dfs ( r, l):
        #     left = left.val
        #     right = right.val
        #     while root:
        #         curr = 0
        #         max_curr = max(curr, max_curr)
                
        
        