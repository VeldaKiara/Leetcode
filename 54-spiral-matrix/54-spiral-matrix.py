'''
time 0(m*n) which is the matrix order of rows and columns, space 0(1)
we set right outside of the matrix since range is non inclusive, 
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #create a list to store the values
        results = [ ]
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix) #no of rows
        
        while left < right and top < bottom:
            #get values in the top row first
            for i in range(left, right):
                results.append(matrix[top][i])
            top += 1 #move top to the next value
            
            #get value of the right column
            for i in range(top, bottom):
                results.append(matrix[i][right - 1]) #return right to bounds
            #shift right to the left
            right -= 1
            
            #in cases where the matrix is a one d like [1,2,3 ] or [
            # [1
            #  2
            #  3]
            if not (left < right and top < bottom):
                break
            #get every value from the bottom, we will need to include the right most value by decreasing by one, since range is non inclusive we will decrease left too, and to move to the left use -1 to reverse
            for i in range(right-1, left - 1, -1):
                results.append(matrix[bottom - 1][i])
            #move the bottom pointer above
            bottom -= 1
            
            #get values of the left column
            #we are move up from bottom, and one value less from the top, in reverse order
            for i in range(bottom - 1, top - 1, -1 ):
                results.append(matrix[i][left])
            #increment left since we want to move to the inner matrix
            left += 1
        return results
       
                
            
            