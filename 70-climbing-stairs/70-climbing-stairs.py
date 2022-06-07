class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = {}
        dp[-1] = 0
        dp[-2] = 0
        def countWays(n):
            if n == 0:
                return 1
            elif n < 0:
                return 0
            if n-1 not in dp:
                dp[n-1] = countWays(n-1)
            if n-2 not in dp:
                dp[n-2] = countWays(n-2)
            return dp[n-1] + dp[n-2]
        return countWays(n)
    