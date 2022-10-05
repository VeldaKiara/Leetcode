# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Use queues, fifo, add elements to the right
add each element per level, node then kids separately

'''
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        store = [ ]
        q = collections.deque( )
        q.append(root)
        
        #bfs
        while q:
            qSize = len(q)
            stage = [ ] #one level at a time, add it
            for i in range(qSize):
                node = q.popleft()
                if node: #non empty
                    stage.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if stage:
                 store.append(stage)
        return store
           
                    
                    
                    
                
                
    
        
        
        
        