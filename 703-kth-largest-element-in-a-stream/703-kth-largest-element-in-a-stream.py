class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.mp = nums
        self.k = k
        heapq.heapify(self.mp)
        while len(self.mp) > k:
            heapq.heappop(self.mp)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.mp, val)
        if len(self.mp) > self.k:
            heapq.heappop(self.mp)
        return self.mp[0]
        
        
        
        
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)