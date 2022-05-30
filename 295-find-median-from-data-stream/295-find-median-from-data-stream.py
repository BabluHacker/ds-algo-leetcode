class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num) # maxheap
        # making sure every num in small <= num in large
        if self.small and self.large and (-1 * self.small[0]) > self.large[0]:
            tmp = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, tmp)
        
        # balance the size of both heap if any one of this is 2 size big
        if len(self.small) > len(self.large) + 1:
            tmp = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, tmp)
        if len(self.large) > len(self.small) + 1:
            tmp = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * tmp)
        

    def findMedian(self) -> float:
        sl = len(self.small)
        ll = len(self.large)
        if sl == ll:
            return (-1*self.small[0] + self.large[0]) / 2
        elif sl > ll:
            return -1 * self.small[0]
        else:
            return self.large[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()