class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #set our left and right boundaries
        left, right = 0, len(matrix) - 1
        
        while left < right:
            for i in range(right - left):
                top, bottom = left, right
                #this is because the matrix is a square
                
                #save the top left value, like hold it and work anticlockwise
                topLeft = matrix[top][left + i]
                
                #move bottom left into top left
                matrix[top][left + i] = matrix[bottom - i][left]
                
                #move bottom right into bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]
                
                #move top right into bottom right
                matrix[bottom][right - i] = matrix[top + i][right]
                
                #move top left into top right
                matrix[top + i][right] =  topLeft
            
            right -= 1
            left += 1
                
                    
                    
               