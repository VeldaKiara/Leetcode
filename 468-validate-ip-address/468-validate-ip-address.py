''' divide and conquer
break down the addresses
check whether the numbers for IPV4 are between 0-255, with no leading zeros
for IPV6, check if each block is between 1 - 4,leading zeros are allowed 
The isdigit() method returns True if all the characters are digits, otherwise False
ipv4, dot, v6, colon
Python all() Function returns True if all items in an iterable are true, otherwise it returns False.
'''
class Solution:
    def valid_Ipv4(self, queryIP: str):
        address = queryIP.split('.')
        for i in address:
            #check if value between 0-255, if len between 1-3
            if len(i) == 0 or len(i) > 3:
                return "Neither"
            #no leading zeros, only digits are allowed, less than 255
            if i[0] == '0' and len(i) != 1 or not i.isdigit() or int(i) > 255:
                return "Neither"
            
        return "IPv4"
    def valid_Ipv6(self, queryIP: str):
        address = queryIP.split(':')
        accepted_hex_digits = '0123456789abcdefABCDEF'
        for i in address:
            #validate hex range, 4 digits in one block, compare with acceped digits
            if len(i) == 0 or len(i) > 4 or not all(h in accepted_hex_digits for h in i ):
                return "Neither"
            
        return "IPv6"
    

    def validIPAddress(self, queryIP: str):
        if queryIP.count('.') == 3:
            return self.valid_Ipv4(queryIP)
        elif queryIP.count(':') == 7:
            return self.valid_Ipv6(queryIP)
        else:
            return "Neither"
        