'''
time O(n) space O(1)
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #using greedy algorithm
        #goal post is the end and keeps shifting
        goalPost = len(nums) - 1
        #since we are working our way backwards, do a range loop
        #we start from the last idx move from  it till the first index
        for i in range(len(nums)-1, -1, -1):
            #nums of i is the jump len, if condition is true we can reach the goal
            if i + nums[i] >= goalPost:
                #update the goal to i that is where we are jumping from
                goalPost = i
                
        return True if goalPost == 0 else False
                
        
        