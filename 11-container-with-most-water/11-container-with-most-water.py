class Solution:
    def maxArea(self, height: List[int]) -> int:
        #temporary store values of the container
        #have two pointers, right and left, move pointers
        #iterate throught the heights to find max area
        #area -= len of shorter vertical line * distance between lines
        current = 0
        left, right = 0, len(height) - 1
        
        while left < right:
            area = (right - left) * min(height[right],height[left])  
            current = max(area, current)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
        return current