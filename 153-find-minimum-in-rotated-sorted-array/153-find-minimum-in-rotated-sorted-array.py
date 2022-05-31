class Solution:
    def findMin(self, nums: List[int]) -> int:
        pivot = self.find_pivot(nums)
        if pivot == -1:
            return nums[0]
        return nums[pivot]
        
    def find_pivot(self, nums):
        s, e = 0, len(nums)-1
        while(s <= e):
            m = s + (e-s)//2
            if m < e and nums[m] > nums[m+1]:
                return m+1
            if m > s and nums[m] < nums[m-1]:
                return m
            
            if nums[m] > nums[e]:
                s = m+1
            else:
                e = m-1
        return -1