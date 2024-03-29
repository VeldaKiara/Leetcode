# class Solution 1:
#     def longestPalindrome(self, s: str) -> str:
#         vel = [[False for i in range(len(s))] for i in range(len(s))]
#         for i in range(len(s)):
#             vel[i][i] = True
#         max_len = 1
#         start = 0
#         for k in range (2, len(s)+1):
#             for i in range (len(s)-k+1):
#                 end = i + k
#                 if  k == 2:
#                     if s[i] == s[end-1]:
#                         vel[i][end-1]=True
#                         max_len = k
#                         start = i
#                 else:
#                     if s[i] == s[end-1] and vel[i+1][end-2]:
#                         vel[i][end-1]=True
#                         max_len = k
#                         start = i
#         return s[start:start+max_len]
"""
create a func pass in the str
initialize the result as an empty string, record longest len of the result
Go through all positions considering it to be the center, 
use pointers for left and right, while in bound and if palindrome if l=r
rem we are starting from the middle to l,r 
update the result and longest result
expand pointers 
Check for even len, check if longest, update the result, expand ooutwards 

"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = " "
        longestResult = 0
        for i in range(len(s)):
            #odd 
            l, r = i, i
            #start in the middle and going outwards
            while l >= 0 and r < len(s) and s[l] == s[r]:
                #check len of the palindrome
                if (r - l + 1) > longestResult:
                    #update result & len
                    result = s[l: r + 1]
                    longestResult = r - l + 1
                #expand pointers
                l -= 1
                r += 1
            
            #even base case
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > longestResult:
                    result = s[l: r + 1]
                    longestResult = r - l + 1
                l -= 1
                r += 1
        return result
                
                    
                
            
        
        
        