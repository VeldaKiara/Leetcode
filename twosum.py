'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
Constraints:
2 <= nums.length <= 105
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        ans = []
        for i in range(len(nums)):
            secondNumber = target-nums[i]
            if(secondNumber in dict.keys()):
                secondIndex = nums.index(secondNumber)
                if(i != secondIndex):
                     return sorted([i, secondIndex])
            dict.update({nums[i]: i})
                    