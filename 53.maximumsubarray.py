class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray = nums[0] #since we will have negative values, and array is non empty
        current_sum = 0 #this will change as we move across the array
        # go through the number in nums
        for num in nums:
            #if we have neg values we will remove them from the sum
            if current_sum < 0: #if sum is negative, reset sum to zero
                current_sum = 0
                # add current number to this
            current_sum += num
            #update max sub array
            max_subarray = max(max_subarray, current_sum)
        return max_subarray