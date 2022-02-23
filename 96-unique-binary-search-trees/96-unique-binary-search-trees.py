'''
dynamic programming
have an initial array with ones, base cases 0 nodes = 1 tree, 1 nodes = 1 tree
'''
class Solution:
    def numTrees(self, n):
        numberTrees = [1] * (n + 1)
        for nodes in range(2, n + 1):
            total= 0
            #consider each value as a root
            for root in range(1, nodes + 1):
                #getting values of subtrees on the right and left
                left = root - 1
                right = nodes - root
                #add to total for each iteration
                total += numberTrees[left] * numberTrees[right] 
            numberTrees[nodes] = total
        return numberTrees[n]
                
                
        
        
        
        