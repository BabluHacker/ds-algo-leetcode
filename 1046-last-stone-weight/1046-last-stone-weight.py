class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-st for st in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)
            
            if x == y:
                continue
            else:
                heapq.heappush(stones, -(y-x))
        
        if len(stones) > 0:
            return -stones[0]
        return 0
            
        