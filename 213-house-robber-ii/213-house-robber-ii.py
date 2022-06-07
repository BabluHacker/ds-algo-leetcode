class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        return max(self.rob_single(nums[1:]), nums[0]+self.rob_single(nums[2:-1]))
        
        
    def rob_single(self, nums):
        dp = {}
        n = len(nums)
        dp[n], dp[n+1] = 0, 0 
        
        def getAmount(i):
            if i not in dp:
                dp[i] = max(getAmount(i+1), nums[i]+getAmount(i+2))
            return dp[i]
        return getAmount(0)