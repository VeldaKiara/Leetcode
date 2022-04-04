'''
sorting through the array O(nlogn) time, n being no.of intervals given
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #we will be sorting a list of pairs so we need to use keys, they will the 
        # first number of the arrays
        intervals.sort(key = lambda i: i[0])
        #storing the intervals initialize with first set to avoid edge cases
        mergedIntervals = [intervals[0]]
        
        #iterate through every single interval from the first index, since the zero is initialized
        for start, end in intervals[1:]:
            #the mergedIntervals gets the most recently added intervals, and get the end value because it is what we need to know if there is an overlap
            lastItemInInterval = mergedIntervals[-1][1]
            if start <= lastItemInInterval:
                #overlapping occured
                #to merge overlaps take the most recent added interval a d ending value of it and set it to the max of itself and current end value we are at
                mergedIntervals[-1][1] = max(lastItemInInterval, end)
            else:
                 mergedIntervals.append([start,end])
        return  mergedIntervals 
            
        