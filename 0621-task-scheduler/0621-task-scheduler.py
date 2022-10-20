"""
max_count - 1 * (n + 1) + max(tasks) 

"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        countss  = list(collections.Counter(tasks).values())
        bun_mx = max(countss)
        output = (bun_mx - 1) * (n + 1) + countss.count(bun_mx)
        return max(len(tasks), output)
      
        
        
        
        
        
        