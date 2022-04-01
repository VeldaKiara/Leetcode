class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            middle = (left + right) // 2
            if target == nums[middle]:
                return middle
            #left sorted portion
            if nums[left] <= nums[middle]:
                if target > nums[middle] or target < nums[left]:
                    #search the right portion
                    left = middle + 1
                else:
                    #search the left pos and update right pointer
                    right = middle - 1
            #right sorted portion
            else:
                if target < nums[middle] or target > nums[right]:
                    #update right pointer
                    right = middle - 1
                else:
                    left = middle + 1
        return -1
                    

                
            
            