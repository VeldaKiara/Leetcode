'''
we need to use a list in this case because order is important.
largest to smallest, order is important hence using nested lists

key things to look on 
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

come up with a custom nested list
have a result 
iterate through the list, symbol and value, in reverse order 
divide the num with the values in the list to determine how many times it gets into the result
this is to be able to know how many times we are adding the symbols


'''
class Solution:
    def intToRoman(self, num: int) -> str:
        symbol_list = [
            ["I", 1], ["IV", 4], ["V", 5], ["IX", 9],
            ["X", 10],["XL", 40],["L", 50], ["XC", 90], 
            ["C", 100], ["CD", 400],["D", 500], ["CM", 900],
            ["M",1000]  
        ]
        result = ""
        for symbol, value in reversed(symbol_list):
            if num // value:
                count = num // value
                result += (symbol * count)
                num = num % value
        return result
        
        