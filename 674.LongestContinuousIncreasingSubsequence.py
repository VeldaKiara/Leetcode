'''
Given an unsorted array of integers nums, return the length of the longest continuous increasing 
subsequence (i.e. subarray). The subsequence must be strictly increasing.
A continuous increasing subsequence is defined by two indices l and
r (l < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, 
nums[i] < nums[i + 1].

solving it 
create var to hold curr val and longest 
loop through the list, to get the subsequence arrays
get the max 

'''

class Solution:
    def findLengthOfLCIS(self, nums):
        current_value = 0
        longest_len = 0

        #edge cases
        if len(nums) <= 1:
            return len(nums)

        for i, j in enumerate(nums):
            if i == 0 or j <= nums[i - 1]:
                current_value = 0
            
            current_value += 1
            longest_len = max(longest_len, current_value)

        return longest_len