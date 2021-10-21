class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        list1 = { }
        for num in nums:
            if num not in list1:
                list1[num] = 1
            else:
                del list1[num]
        return list(list1.keys())[0]

