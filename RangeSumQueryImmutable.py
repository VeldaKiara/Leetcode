class NumArray:
    '''
    i used accumulative frequency to solve this problem.
    where the solution adds all the numbers in the various indices adding a zero at the beginning, because we don't want
    we want to be able to substract the beginning and the end of the array.
    this is the look up 
    '''
    def __init__(self, nums: List[int]):
        self.accumulative_frequency = [0] + list(accumulate(nums))
        

    def sumRange(self, left: int, right: int) -> int:
        '''
        we add one to the right to be inclusive of the first number
        '''
        return self.accumulative_frequency[right + 1] - self.accumulative_frequency[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
