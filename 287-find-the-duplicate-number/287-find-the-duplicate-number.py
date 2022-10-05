class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        store = set()
        for i in nums:
            if i in store:
                return i
            store.add(i)
    
#     def findDuplicate(self, nums: List[int]) -> int:
#         back = 0
#         front = 1
#         n = len(nums)
#         nums.sort()
#         while front <= n-1:
#             if nums[back] == nums[front]:
#                 return nums[back]
#             else:
#                 back += 1
#                 front += 1
#         if len(nums) <= 1:
#             return False

#         slow, fast = nums[0], nums[nums[0]]

#         while slow != fast:
#             slow, fast = nums[slow], nums[nums[fast]]
#         slow = 0
#         while slow != fast:
#             print(nums[slow], nums[fast])
#             slow, fast = nums[slow], nums[fast]
#         return slow

    
    


        
        
            