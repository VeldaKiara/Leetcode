class Solution:
    '''
    create var to loop through the array
    create left and right array
    calculate the product of both
    return the output
    '''
    def productExceptSelf(self, nums):
        # products = [1 for _ in range(len(nums))]
        products = [1] * len(nums)
        leftCurrentProducts = 1
        for i in range(len(nums)):
            products[i] *= leftCurrentProducts
            leftCurrentProducts *= nums[i]
        rightCurrentProducts = 1
        for i in reversed(range(len(nums))):
            products[i] *= rightCurrentProducts
            rightCurrentProducts *= nums[i]
        return products


            
    
            
        
            
    
                
     