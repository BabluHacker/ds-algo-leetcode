class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n+1)
        dp[0] = 0
        squares = [i*i for i in range(1, n+1)]
        
        for target in range(1, n+1):
            for square in squares:
                if target - square < 0:
                    break
                dp[target] = min(dp[target], 1 + dp[target-square])
        return dp[target]
    
    