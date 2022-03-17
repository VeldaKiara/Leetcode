class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #use two pointers
        #check if the sum is less than greater than or equal to targets sum, 
        #if less than, move the left pointer, if greater move the right, equal
        #is the target sum
        #return index of number that lead to target sum, they are based on one so add 1 to each of the pointers
        l, r = 0, len(numbers) - 1
        while l < r:
            sumNumbers = numbers[l] + numbers[r]
            if sumNumbers > target:
                r -= 1
            elif sumNumbers < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return [ ]
        
        