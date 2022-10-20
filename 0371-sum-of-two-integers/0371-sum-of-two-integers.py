'''
func getSum(a int, b int) int {
    
    for b != 0 {
        carry := a & b
        fmt.Println(carry)
        a = a ^ b
        b = carry << 1
    }
    return a
}
'''
# class Solution:
#     def getSum(self, a: int, b: int) -> int:
#         while b != 0:
#             addition = a & b
#             a = a ^ b
#             b = addition << 1
#         return a   
    
class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        # 32 bit mask in hexadecimal
        mask = 0xffffffff
        
        # works both as while loop and single value check 
        while (b & mask) > 0:
            
            carry = ( a & b ) << 1
            a = (a ^ b) 
            b = carry
        
        # handles overflow
        return (a & mask) if b > 0 else a