'''
using hashmaps 

'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_ems = collections.Counter(nums)
        return max(count_ems.keys(), key=count_ems.get)
        
        
        
            






# '''
# the brute force algorithm by counting the number of 
# occurences other solutions
# '''
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         majority_counts = len(nums)//2
#         for num in nums:
#             counts = sum(1 for i in nums if i == num)   
#             if counts > majority_counts:
#                 return num
            

        