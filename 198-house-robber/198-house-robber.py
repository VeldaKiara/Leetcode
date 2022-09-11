"""
dynamic programming, Google likes this topic 
constraint, we cannot rob two houses consecutively
have two variables
iterate through the houses and get max of how many houses we can rob
we will have rob 1 and rob 2
rob 1 is the first house is the street
rob 2 is the second house is the street
since we cannot rob two houses consecutively, we will need to have a temp storage to store the max values in this case #[rob1, rob2, n, n+1]
rob 1 will be added to n to show there is a gap between the houses
if we want to rob 1 we will rob n as well and if we want to rob 2 we will rob n+1
we iterate to the next position for rob 1 to be equal to rob 2
rob 2 returns the temp storage
we return rob 2 because its going to be at the end of the list
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for i in nums:
            temporary_values = max(i + rob1, rob2)
            rob1 = rob2
            rob2 = temporary_values
        return rob2
        
        
        
        