'''
start merging elements from the last item
merge in reverse order
loop to check if the lists are not empty
account for left over numbers from nums2

'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last_index = m + n - 1
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last_index] = nums1[m - 1]
                m -= 1
            else:
                nums1[last_index] = nums2[n - 1]
                n -= 1
                
            last_index -= 1
        while n > 0:
            nums1[last_index] = nums2[n - 1]
            n, last_index = n - 1, last_index - 1
            
            
        
        