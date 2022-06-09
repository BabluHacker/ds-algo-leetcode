class Solution:
    
    
    def maxProduct(self, nums: List[int]) -> int:
        curMin, curMax = 1, 1
        res = max(nums)
        for n in nums:
            tmp = curMax * n
            curMax = max(n*curMax, n*curMin, n)
            curMin = min(tmp, n * curMin, n)
            res = max(curMax, res)
        return res