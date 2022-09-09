'''
using hashmaps 
store the number of times an element appears, then return the max

'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_ems = collections.Counter(nums)
        return max(count_ems.keys(), key=count_ems.get)
        
        

            

        