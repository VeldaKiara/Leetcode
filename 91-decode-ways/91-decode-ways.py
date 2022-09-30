'''
create a dict to store alphabets 
decision trees, 
preceeding zero's are invalid
edge cases include numbers above 26
 alphabets = [ 
            'A': '1', 'B': '2', 'C':'3', 'D':'4', 'E':'5', 'F':'6','G':'7',
            'H':'8','I':'9','J':'10','K':'11', 'L':'12', 'M':'13', 'N':'14', 
            'O':'15', 'P':'16', 'Q':'17', 'R':'18', 'S':'19', 'T':'20', 
            'U':'21', 'V':'22','W':'23', 'X':'24','Y':'25','Z':'26'
        ]
if not a zero, value is btwn 0-9    
check if double digit is btwn 10-26 
cache the result then return it O(n) time
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        #initialize the cache and map to one, base case get an empty string should return 1
        alpha = {len(s):1}
        #Recursive
        def decode(i):
            #if num cached or last pos in string
            if i in alpha:
                return alpha[i]
            #if not end of string, has preceeding zero
            if s[i] == "0":
                return 0
            #sub problems, single digit and double digit
            result = decode(i + 1)
            if (i + 1 < len(s) and (s[i]=="1" or s[i]=="2" and s[i + 1] in "0123456")):
                result += decode(i + 2)
            alpha[i] = result
            return result
        return decode(0)
                
            
            
            
            
            
            
            
        
    