class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for i in range(len(points)):
            d = self.distance(points[i])
            points[i].insert(0, d)
      
        heapq.heapify(points)
        ans = []
        for _ in range(k):
            p = heapq.heappop(points)
            ans.append([p[1], p[2]])
        return ans
    
    def distance(self, point):
        return point[0] ** 2 + point[1] ** 2