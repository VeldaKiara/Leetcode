class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #recursive function
        result  = [ ]
        def depthFirstSearch(i, current, total):
            #base cases, cur is the combination
            #if we find the target
            if total == target:
                #we still want to continue recursively so return the copy
                result.append(current.copy())
                return
            #if we do not find a combination, if i is out of bounds
            if i >= len(candidates) or total > target:
                return
            #the recursive step, back tracking
            #include values of candidates i, to include values
            current.append(candidates[i])
            depthFirstSearch(i, current, total + candidates[i])
            #pop the current decision, to add the next decision
            current.pop()
            #add the next decision, if we are not going to include candidate[i]
            depthFirstSearch(i + 1, current, total)
            
            
        #call the func
        depthFirstSearch(0, [], 0)
        return result
        
            
            
        
            
            
        
        