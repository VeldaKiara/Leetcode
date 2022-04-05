''''
time O(n) space O(n)
'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        results = [ ]
        #iterate through the input
        for i in range(len(intervals)):
            #edge case if the interval goes beyond the interval where we are at
            #1 is for the last value of intervals, 0 is for first
            if newInterval[1] < intervals[i][0]:
                results.append(newInterval)
                return results + intervals[i:]
            #if interval goes after the current interval we are currently at
            elif newInterval[0] > intervals[i][1]:
                results.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
                
        results.append(newInterval)
        return results