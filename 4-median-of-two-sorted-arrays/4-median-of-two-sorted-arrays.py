class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # merge both array
        m = len(nums1)
        n = len(nums2)
        nums = self.merge(nums1, nums2, m, n)
        l = m + n
        if l % 2 == 0:
            mid = l//2
            median = (nums[mid]+ nums[mid-1])/2
        else:
            median = nums[l//2]
        return median
        
    def merge(self, nums1, nums2, m, n):
        
        
        p1 = p2 = 0
        nums = []
        
        for i in range(m+n):
            if p2 >= n or (p1 < m and nums1[p1] <= nums2[p2]):
                nums.append(nums1[p1])
                p1 += 1
            else:
                nums.append(nums2[p2])
                p2 += 1
                
        return nums