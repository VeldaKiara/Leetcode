'''
brute force 
step 1: create a func to return full binary trees, 
handle base cases, n==0, return an empty list and n==1, return a list with a single node
step 2: create a list,one of the nodes (n) will be a root node, and the n-1 will be the rest of the nodes
step 3: calculate the number of left nodes we will have using range, calculate the number of nodes we will have on the right, control flow for loops
step4: recurse the function to return lists of all possible trees
step5: look thorugh all the possible lists to make full BST's through making a nested for loop


'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Before caching
'''
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        def allTrees(n):
            if n == 0:
                return []
            if n == 1:
                return [TreeNode()]
            listTrees = [ ]
            for left in range(n): 
                # 0-(n-1)
                right = n - 1 - left
                #going thru all combinations
                leftTrees, rightTrees = allTrees(left), allTrees(right)
                #bst we could make
                for tree1 in leftTrees:
                    for tree2 in rightTrees:
                        #all root vals start with 0
                        listTrees.append(TreeNode(0, tree1,tree2))
                        
            return listTrees
        return allTrees(n)
'''
#after caching
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        #map n to the full btrees
        fullBinaryTrees = { 0 : [ ], 1: [TreeNode()]}
        def allTrees(n):
            if n in fullBinaryTrees:
                return fullBinaryTrees[n]
            listTrees = [ ]
            for left in range(n): 
                ''' 0-(n-1)'''
                right = n - 1 - left
                #going thru all combinations
                leftTrees, rightTrees = allTrees(left), allTrees(right)
                #bst we could make
                for tree1 in leftTrees:
                    for tree2 in rightTrees:
                        #all root vals start with 0
                        listTrees.append(TreeNode(0, tree1,tree2))
            fullBinaryTrees[n] = listTrees           
            return listTrees
        return allTrees(n)

                
            
        