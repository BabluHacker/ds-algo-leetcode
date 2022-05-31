class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        pivot = self.find_pivot(nums)
        if pivot == -1:
            return self.b_search(nums, 0, len(nums)-1, target)
        if target >= nums[0]:
            return self.b_search(nums, 0, pivot, target)
        return self.b_search(nums, pivot+1, len(nums)-1, target)
        
    def b_search(self, nums, s, e, target):
        if s > e : return False
        
        m = s + (e-s)//2
        if nums[m] == target:
            return True
        if nums[m] < target:
            return self.b_search(nums, m+1, e, target)
        else:
            return self.b_search(nums, s, m-1, target)
        
        
        
    def find_pivot(self, nums):
        s, e = 0, len(nums)-1
        while (s <= e):
            m = s + (e-s)//2
            
            if m < e and nums[m] > nums[m+1]:
                return m 
            if m > s and nums[m] < nums[m-1]:
                return m-1
            
            if nums[s] == nums[m] and nums[m] == nums[e]:
                # when all s, e, m are equal then just move s and e
                # NOTE: what if s and e are pivot decreasing slop , just check before moving
                if s < e and nums[s] > nums[s+1]:
                    return s
                s += 1
                if s < e and nums[e] < nums[e-1]:
                    return e - 1
                e -= 1
                
            # left side from mid sorted, then pivot is on the right
            # to find if sorted, s < m or there might be a case s==m where need to check m>e because all right elm are smaller than left and mid is in the left side. there will not be s > m bcz it will then indicate right is sorted
            elif nums[s] < nums[m] or (nums[s] == nums[m] and nums[m] > nums[e]):
                s = m+1
            else:
                e = m-1
        return -1