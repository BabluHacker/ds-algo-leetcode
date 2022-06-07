class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = {}
        def countWays(n):
            if n == 0:
                return 1
            elif n < 0:
                return 0
            if n-2 not in dp:
                dp[n-2] = countWays(n-2)
            if n-1 not in dp:
                dp[n-1] = countWays(n-1)
            return dp[n-1] + dp[n-2]
        return countWays(n)
    