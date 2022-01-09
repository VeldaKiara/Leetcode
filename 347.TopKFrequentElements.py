'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Constraints:

1 <= nums.length <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

'''

'''
first of all create a hashmap 
store the frequencies of the numbers 
get the largest 

'''
from collections import Counter
class Solution:
    def topKFrequent(self, nums, k):
        if k == len(nums):
            return nums
        
        #hashmap to create char and how often it appears
        count = Counter(nums)
        
        #build a heap of top k elements and convert to output array
        return heapq.nlargest(k, count.keys(), key=count.get)
        
        