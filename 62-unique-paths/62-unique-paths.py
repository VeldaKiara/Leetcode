'''
time O(m * n)
space O(n)
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #start with the bottom row
        row = [1] * n
        #go through all the other rows
        for i in range(m - 1):
            #this will be above the previous row
            newRow = [1] * n
            #to avoid out of bounds edge case
            #last items on right will always have one move, bottom
            for j in range(n - 2, -1,-1):
                newRow[j] = newRow[j + 1] + row[j]  
            row = newRow
        return row[0]
        