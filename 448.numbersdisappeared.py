class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length_nums = len(nums)
        set_numbers = set(range(1, length_nums + 1))
        for num in nums:
            if num in set_numbers:
                set_numbers.remove(num)
        return list(set_numbers)
    
''' 
used set since it does not accept duplicates, used len as range and added one 
for inclusivity, looped through the list, if item in set removed and we are left with what is not there, then cast the set back to a list
'''