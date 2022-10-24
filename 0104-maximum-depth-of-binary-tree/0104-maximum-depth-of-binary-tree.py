# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # recursion
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     #DFs, recursive, left + right
    #     if not root:
    #         return 0
    #     return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    #bfs using queues
     def maxDepth(self, root: Optional[TreeNode]) -> int:
        #DFs, recursive, left + right
        if not root:
            return 0
        curr_level = 0
        line = deque([root])
        while line:
            #go through the queue removing every element in it 
            for i in range(len(line)):
                node = line.popleft()
                if node.left:
                    line.append(node.left)
                if node.right:
                    line.append(node.right)
            curr_level += 1
        return curr_level
      
                    
                    
                    
                
            
    
    
       
                
        
        