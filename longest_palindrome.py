# Given a string s, return the longest palindromic substring in s.
# Constraints: 1 <= s.length <= 1000
# s consist of only digits and English letters (lower-case and/or upper-case)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        vel = [[False for i in range(len(s))] for i in range(len(s))]
        for i in range(len(s)):
            vel[i][i] = True
        max_len = 1
        start = 0
        for k in range (2, len(s)+1):
            for i in range (len(s)-k+1):
                end = i + k
                if  k == 2:
                    if s[i] == s[end-1]:
                        vel[i][end-1]=True
                        max_len = k
                        start = i
                else:
                    if s[i] == s[end-1] and vel[i+1][end-2]:
                        vel[i][end-1]=True
                        max_len = k
                        start = i
        return s[start:start+max_len]

# How I solved it 
# Define one square matrix of order same as the length of string, and fill it with False
# Set the major diagonal elements as true, so Vel[i, i] = True for all i from 0 to order – 1
# start := 0
# for k in range 2 to length of S + 1
# for i in range 0 to length of S – k + 1
# end := i + k
# if k = 2, then
# if S[i] = S[end - 1], then
# vel[i, end - 1] = True, max_len := k, and start := i
# otherwise
# if S[i] = S[end - 1] and vel[i + 1, end - 2], then
# vel[i, end - 1] = True, max_len := k, and start := i
# return a substring of from index start to start + max_len
