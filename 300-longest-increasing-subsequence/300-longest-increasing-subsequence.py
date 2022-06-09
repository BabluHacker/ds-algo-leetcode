class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [1 for _ in range(len(nums))]
        res = []
        max_res = 1
        for i in range(1, len(nums)):
            dummy = []
            for j in range(0, i):
                if nums[j] < nums[i]:
                    # for storing elements LIS
                    if dp[i] < 1+dp[j]:
                        dummy.append(nums[j])
                        dp[i] = 1+dp[j]
                    # dp[i] = max(dp[i], 1+dp[j])
                    
            dummy.append(nums[i])
            # print(nums[i], dummy)
            if max(dp) == dp[i]:
                res = dummy.copy()
        
        print(res)
                    
        return max(dp)
