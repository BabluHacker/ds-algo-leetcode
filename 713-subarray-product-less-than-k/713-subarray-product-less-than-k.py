class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0
        left, ans = 0, 0
        n = len(nums)
        cur_prod = 1
        
        for right, num in enumerate(nums):
            cur_prod *= num
            while cur_prod >= k:
                cur_prod /= nums[left]
                left += 1
            ans += right - left + 1
                    
        return ans