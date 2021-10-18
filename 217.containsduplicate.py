class Solution:
    def ContainsDuplicate(self, nums):
        store = [ ]
        for num in nums:
            if num in store:
                return True
            else:
                store.append(num)
          
li = Solution( )
print(li.ContainsDuplicate([ 2,3,4,5,6,6,7]))

