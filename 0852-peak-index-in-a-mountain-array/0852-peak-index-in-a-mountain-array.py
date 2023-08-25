'''
Binary search 
we use binary search to solve this problem. We create an integer l and initialize it to the starting index 0. We also create another integer variable r and set it to the last index of arr, i.e., arr.length - 1.
We get the middle of the range mid = (l + r) / 2 and compare arr[mid] with the next element. If arr[mid] < arr[mid + 1], we move to the upper half of the range by setting l = mid + 1 as our peak index is definitely greater than mid. Otherwise, if arr[mid] > arr[mid + 1], we move to the lower half of the range by setting r = mid as the peak index is either mid or some index smaller than mid.

The answer would be within the range (l, r) at any point. All the indices smaller than l are indices smaller than the peak index and all indices greater than r are indices greater than the peak index. We continue the search as long as l < r.

When l == r, l (or r) denotes the required peak index.

Create two integer variables l and r to store the solution space of the problem. We initialize l with 0 and r to arr.length - 1.
While l < r:
Get the index of the middle element using mid = (l + r) / 2.
If arr[mid] < arr[mid + 1], it indicates peak index is greater than mid. As a result, we move to upper half of the range by setting left = mid + 1.
Else, if arr[mid] >= arr[mid + 1], it indicates that the peak index is either mid or some index smaller than mid. As a result, we move to the lower half of the range by setting r = mid.
Return l (or r as both are equal now).


'''

# class Solution:
#     def peakIndexInMountainArray(self, arr: List[int]) -> int:
#         l = 0
#         r = len(arr)
#         while l < r:
#             mid = (l + r) // 2
#             if arr[mid] < arr[mid + 1]:
#                 l = mid + 1
#             else:
#                 r = mid
#         return l

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        i = 0
        while arr[i] < arr[i + 1]:
            i += 1
        return i
        
        