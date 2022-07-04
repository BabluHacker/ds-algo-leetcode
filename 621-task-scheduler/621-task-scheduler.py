class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        
        q = deque()
        time = 0
        while maxHeap or q:
            # pop from maxHeap that is the most occurred value
            # push into q with idletime to track that 
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt: # if non-zero
                    q.append([cnt, time+n])

            # check on q if any idle time finished
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        
        return time
        