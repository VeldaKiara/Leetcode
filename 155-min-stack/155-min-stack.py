'''
have two stacks 
one to store the minimum and the other to store the regular stack values
if we pop we do it on both
we use two stacks to be able to keep track of the minimum value, since we also want to get to O(1) time


'''

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = [ ]
        self.minimum_stack = []
    
          
    def empty(self):
        return len(self.stack) == 0
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minimum_stack[-1] if self.minimum_stack else val)
        return self.minimum_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minimum_stack.pop()  

    def top(self) -> int:
        return self.stack[-1]   

    def getMin(self) -> int:
        return self.minimum_stack[-1]
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()