'''
the trick is getting how manu 5's there are to know how many zeroes there are

'''
class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 0
        while n != 0:
            n = n//5
            result += n
        return result
        
        
        
        