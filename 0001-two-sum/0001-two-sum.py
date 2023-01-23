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