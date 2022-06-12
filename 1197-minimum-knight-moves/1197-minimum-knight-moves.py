class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        
        visit = set()        
        queue = deque([(0,0)])
     
        visit.add((0,0))
        x = abs(x)
        y = abs(y)
        dx = [2,1,-2,-1,2,1]
        dy = [1,2,1,2,-1,-2]
        steps = 0
        while queue:
            level = len(queue)
            for j in range(level):
                
                n = queue.popleft()
                if n == (x,y):
                    return steps
                for i in range(6):
                    node = (n[0]+dx[i], n[1]+dy[i])
                    if node not in visit :
                        visit.add(node)
                        queue.append(node)
            steps += 1
        return -1
                
                
            