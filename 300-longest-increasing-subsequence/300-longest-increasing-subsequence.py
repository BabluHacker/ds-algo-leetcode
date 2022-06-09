class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        
        for i in range(1, len(nums)):
            for j in range(0, i):
                
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1+dp[j])
            print(i, dp[i])
                    
        return max(dp)
        