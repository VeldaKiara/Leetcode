'''
The ord() method in Python converts a character into its Unicode code value.
'''
#time complexity O(m*n) where m is number of elements in the strs, n is the len per word
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create a hashmap, map the character count to a list of anagrams, 
        # results = {}  change it to use a default dict to use a list to not deal with an edge case
        results = defaultdict(list)
        
        for i in strs:
            #count characters in each word
            #initial values wil be 0 *26 , one for each character in the alphabet
            count = [0] * 26
            # go through all characters in each string in the word
            for char in i:
                #count the values, to do this we need a to be index 0 and z to be index 25
                count[ord(char) - ord('a')] += 1 #increment based on the number of values we get
            results[tuple(count)].append(i)
        return results.values()
                
                
                
                
                
            
        
        