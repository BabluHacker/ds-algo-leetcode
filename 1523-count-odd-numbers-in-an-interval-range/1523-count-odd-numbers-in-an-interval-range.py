class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (low%2 + high%2 + high-low)//2