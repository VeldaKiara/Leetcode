class Solution:
    def climbStairs(self, n: int) -> int:
        num_ways = { 1:1, 2:2, 3:3}
        for v in range(4, n + 1):
            num_ways[v] = num_ways[ v - 1] + num_ways[ v - 2]
        return (num_ways[n])