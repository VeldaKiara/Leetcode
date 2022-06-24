class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        store = { }
        for num in nums:
            if num in store:
                return True
            else:
                store[num] = "number"
               
