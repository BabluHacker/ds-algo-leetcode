class MedianFinder:

    def __init__(self):
        self.small = [] # max heap
        self.large = [] # min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1*num)
        # making sure every elm in small is less than large
        if self.small and self.large and -1*self.small[0] > self.large[0]:
            tmp = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, tmp)
        # balance 2 heaps
        if len(self.small) - len(self.large) >= 2 :
            tmp = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, tmp)
        elif len(self.large) - len(self.small) >= 2:
            tmp = heapq.heappop(self.large)
            heapq.heappush(self.small, -1*tmp)
    
        
        
        

    def findMedian(self) -> float:
        l1 = len(self.small)
        l2 = len(self.large)
        if l1 == l2:
            return (-1* self.small[0] + self.large[0])/2
        elif l1 > l2:
            return -1 * self.small[0]
        else:
            return self.large[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()