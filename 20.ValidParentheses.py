'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


simple explanation
 create var to hold the closing and opening brackets to keep code clean
 create a dict to hold the matching brackets to be compared 
 create a stack,whenver you find opening bracket keep it
   whenever you find a closing bracket that 
 you can pair with another opening bracket, pop it, 
 check if the stack is empty first, if it is return False
 if the last element in stack matches pop it, else return False
 also return len of stack equal to zero to return True/ False

 time comlexity  O(n)
 space complexity O(n) n being number of brackets
'''

class Solution:
    def isValid(self, s):
        openingBrackets = "({["
        closingBrackets = ")}]"
        matchingBrackets = { ")":"(", "}":"{", "]":"["}
        stack = [ ]
        
        for bracket in s:
            if bracket in openingBrackets:
                stack.append(bracket)
            elif bracket in closingBrackets:
                if len(stack) == 0:
                    return False
                if stack[-1] == matchingBrackets[bracket]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0