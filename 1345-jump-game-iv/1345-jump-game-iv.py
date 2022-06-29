class Solution:
    def __init__(self):
        self.g = defaultdict(list)
        
    def minJumps(self, arr: List[int]) -> int:
        self.construct(arr)
        
        q = [0]
        visit = set()
        visit.add(0)
        n = len(arr)
        level = 0
        while q:
            qlen = len(q)
            
            for i in range(qlen):
                
                curr = q.pop(0)
                if curr == n-1:
                    return level
                #left
                if curr-1 >= 0 and curr-1 not in visit:
                    q.append(curr-1)
                    visit.add(curr-1)

                #right
                if curr+1 < n and curr+1 not in visit:
                    q.append(curr+1)
                    visit.add(curr+1)


                #next in g
                for j in self.g[arr[curr]]:
                    if j not in visit:
                        q.append(j)
                        visit.add(j)
                self.g[arr[curr]].clear()
                
            level += 1
        return 0
    
    def construct(self, arr):
        for i in range(len(arr)):
            self.g[arr[i]].append(i)
    