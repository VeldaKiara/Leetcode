'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product 
of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

'''
class Solution:
    '''
    create var to loop through the array
    create left and right array, solve them in place
    return the output
    '''
    def productExceptSelf(self, nums):
        products = [1 for _ in range(len(nums))]
        
        leftCurrentProducts = 1
        for i in range(len(nums)):
            products[i] *= leftCurrentProducts
            leftCurrentProducts *= nums[i]
            
        rightCurrentProducts = 1
        for i in reversed(range(len(nums))):
            products[i] *= rightCurrentProducts
            rightCurrentProducts *= nums[i]
            
        return products
            
    