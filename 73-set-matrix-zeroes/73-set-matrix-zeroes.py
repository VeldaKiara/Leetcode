class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #get the number of rows and columns
        Rows, Columns = len(matrix), len(matrix[0])
        #extra var to tell us if the first number is zeroed out
        rowZeroed = False
        #determine which rows and columns need to be zeroed
        for r in range(Rows):
            for c in range(Columns):
                if matrix[r][c] == 0 :
                    matrix[0][c] = 0
                    if r > 0:
                         matrix[r][0] = 0
                        
                    else:
                        rowZeroed = True
                        
        #check for every row column pair, by skipping the first row
        for r in range(1, Rows):
            for c in range(1, Columns):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
                    
        #zero out the first row and column if needed
        if matrix[0][0] == 0:
            for r in range(Rows):
                matrix[r][0] = 0
        if rowZeroed:
            for c in range(Columns):
                matrix[0][c] = 0
                