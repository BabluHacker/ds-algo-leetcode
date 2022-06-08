class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        dp[0] = 0
        def dfs(n):
            
            if n not in dp:
                min_coin = sys.maxsize 
                for i in range(len(coins)-1, -1, -1):
                    if n-coins[i] >= 0:
                        min_coin = min(min_coin, 1+dfs(n-coins[i]))
                dp[n] = min_coin
            return dp[n]
        
        res = dfs(amount)
        return res if res < sys.maxsize else -1
            