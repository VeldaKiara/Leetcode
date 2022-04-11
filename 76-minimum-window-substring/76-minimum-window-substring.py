class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #handle edge case in case if empty as shown
        if t == "":
            return " "
        #Create two windows one with current values and the second with values required
        countT, window = {}, {}
        #initialize our count T
        for cha in t:
            #char may not have been added yet so we use get and assign default values
            countT[cha] = 1 + countT.get(cha, 0)
        #what we current have, what we need
        current, need = 0, len(countT)
        #-1 and -1 for right and left
        result,resultLen = [-1, -1], float("infinity")
        #iterate through every character in s
        left = 0
        for right in range(len(s)):
            #new var to store s at r
            cha = s[right]
            #if c has never been added to window, it will get it 
            window [cha]= 1 + window.get(cha,0)
            
            #if we satisfy the condition of what we are looking for
            if cha in countT and window[cha] == countT[cha]:
                current += 1
                #loop to see if the current and need are equal
                while current == need:
                    #update the result by calculating size of the window
                    if ( right - left + 1) < resultLen:
                        result = (left,right)
                        resultLen = ( right - left + 1)
                    #making the list smaller by popping from the left of our window
                    window[s[left]] -= 1
                    if s[left] in countT and window[s[left]] < countT[s[left]]:
                        current -= 1
                    left += 1
                    
        left,right = result
        return s[left:right+1] if resultLen != float("infinity") else ""
                    
                        
                        
                    
                    
                    
                