'''
Dynamic programming issue

'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #define the max val, initialize it as the defaul numbers
        dynamo = [amount + 1] * (amount + 1)
        #edge case of calculating amount at zero
        dynamo[0] = 0
        
        #loop through the items of the list, start at 1 
        for v in range(1, amount + 1):
            for k in coins:
                if v - k >= 0:
                    dynamo[v] = min(dynamo[v], 1 + dynamo[v - k])
        return dynamo[amount] if dynamo[amount] != amount + 1 else -1
                    