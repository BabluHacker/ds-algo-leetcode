class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        n = len(nums)
        dp[n] = 0 
        dp[n+1] = 0
        def find(i):
            if i in dp:
                return dp[i]
            first = nums[i] + find(i+2)
            sec = find(i+1)
            dp[i] = max(first, sec)
            return dp[i]
        return find(0)