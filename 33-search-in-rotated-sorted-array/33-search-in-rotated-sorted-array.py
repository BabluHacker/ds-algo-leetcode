class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = self.find_pivot(nums)
        # print(pivot)
        if pivot == -1:
            return self.b_search(nums, 0, len(nums)-1, target)
        if target >= nums[0]: # 1st half
            return self.b_search(nums, 0, pivot, target)
        return self.b_search(nums, pivot+1, len(nums)-1, target)
    
        
    def b_search(self, nums, s, e, target):
        if s > e : return -1
        m = s + (e-s)//2
        if nums[m] == target: 
            return m
        if nums[m] > target:
            return self.b_search(nums, s, m-1, target)
        else:
            return self.b_search(nums, m+1, e, target)
        
        
    def find_pivot(self, nums):
        s, e = 0, len(nums)-1
        
        while(s <= e):
            m = s + (e-s)//2
            if m < e and nums[m] > nums[m+1]:
                return m
            if m > s and nums[m] < nums[m-1]:
                return m-1
            
            if nums[m] > nums[e]:
                s = m+1
            else:
                e = m-1
        
        return -1
    