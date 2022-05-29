class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # greedy approach
        
        buy = prices[0]
        max_profit = 0
        
        for i in range(1, len(prices)):
            if buy > prices[i]:
                buy = prices[i]
            max_profit = max(max_profit, prices[i]-buy)
        return max_profit
    