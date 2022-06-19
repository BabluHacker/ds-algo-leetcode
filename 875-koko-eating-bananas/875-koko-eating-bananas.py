class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        
        while low <= high:
            m = low + (high-low)//2
            if self.findHourToEat(piles, m) > h:
                low = m+1
            else:
                high = m-1
        return low
            
    
    def findHourToEat(self, piles, k):
        hour = 0
        for c in piles:
            hour += math.ceil(c/k)
        return hour
    
    