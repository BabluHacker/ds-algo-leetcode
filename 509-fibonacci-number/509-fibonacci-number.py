class Solution:
    def fib(self, n: int) -> int:
        dp = {}
        dp[0], dp[1] = 0, 1
        
        def find(num):
            if num in dp: return dp[num]
            dp[num] = find(num-1) + find(num-2)
            return dp[num]
        return find(n)