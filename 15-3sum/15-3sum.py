class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #create a list to hold outputs
        result = [ ]
        #sort the list
        nums.sort()
        #iterate through the index and value
        for i, j in enumerate(nums):
            #to avoid resusing the same value 
            if i > 0 and j == nums[i - 1]:
                continue
            #use two pointers to get the next two values
            left, right = i + 1, len(nums) - 1
            #pointers cannot be equal thus:
            while left < right:
                #compute sum
                threeSum = j + nums[left] + nums[right]
                #check the sums to zero
                if  threeSum > 0:
                    #decrement right
                    right -= 1
                elif threeSum < 0:
                    #increment left
                    left += 1
                else:
                    #update the results with the 3 numbers
                    result.append([j, nums[left], nums[right]])
                    #update the left pointer to avoid same values
                    left += 1
                    #to avoid same values and also avoid left being bigger than the right
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return result
                    
                
        
      
        return [ ]
        