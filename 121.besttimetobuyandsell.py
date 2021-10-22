class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy left, sell right
        left, right = 0, 1 
        # default case
        max_profit = 0 
        #iterate through prices while our right corner has not passed the
        # the end of prices
        #iterate the right side while our right has not passed the end of prices
        
        while right < len(prices):
            #check if profitable
            if prices[ left] < prices [ right]:
                profit = prices[right] - prices [ left]
                #check for the  max of the current max profit with profit, the max ofboth
                #will be th new max profit, if not remains the same
                max_profit = max(max_profit, profit)
                #if not profitable
            else:
                #update values we want our left to be at the lowest value, that is 
                #all the way to the right
                left = right
            right += 1
        return max_profit