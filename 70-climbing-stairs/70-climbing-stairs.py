class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        dp[1] = 1
        dp[2] = 2
        dp[0] = 0
        
        def find_ways(n):
            if n in dp:
                return dp[n]
            
            dp[n] = find_ways(n-1) + find_ways(n-2)
            
            return dp[n]
        return find_ways(n)
            
             