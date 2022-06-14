class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visit = set()
        q = [start]
        visit.add(start)
        dist = {}
        # dist[start] = 0
        n = len(arr)
        while q:
            i = q.pop(0)
            if arr[i] == 0:
                return True
            
            # forward
            if i+arr[i] not in visit and i+arr[i] < n:
                visit.add(i+arr[i])
                q.append(i+arr[i])
                # dist[i+arr[i]] = 1+dist[i]
            
            # backward
            if i-arr[i] not in visit and i-arr[i]>=0:
                    visit.add(i-arr[i])
                    q.append(i-arr[i])
                    # dist[i-arr[i]] = 1+dist[i]
                    
            
        return False