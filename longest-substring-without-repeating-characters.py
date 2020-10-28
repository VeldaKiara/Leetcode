'''question Given a string s, find the length of the longest substring 
without repeating characters.
Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        v =0    #map to store information v and k
        k = 0
        m ={}   
        result = 0
        while k < len(s):
            if s[k] not in m or v>m[s[k]]:
                result = max(result,(k-v+1))
                m[s[k]] = k
            else:
                    v = m[s[k]]+1
                    result = max(result,(k-v+1))
                    k-=1
            k+=1
        return result
    
#used sliding window to solve this problem