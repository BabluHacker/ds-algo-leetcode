class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = self.binarySearchLow(nums, target, True)
        h = self.binarySearchLow(nums, target, False)
        return [l,h]
        
    def binarySearchLow(self, nums, target, findFirst):
        ans = -1
        start, end = 0, len(nums)-1
        
        while start <= end:
            m = start + (end-start)//2
            if nums[m] < target:
                start = m+1
            elif nums[m] > target:
                end = m-1
            else:
                # potential ans found
                ans = m
                if findFirst:
                    end = m-1
                else:
                    start = m+1
        return ans
                