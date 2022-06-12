class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        INF = 2147483647
        
        fx = [0, 0, 1, -1]
        fy = [1, -1, 0, 0]
        m = len(rooms)
        n = len(rooms[0])
        
        q = list()
        
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i,j))
        
        while q:
            ux, uy = q.pop(0)
            
            for k in range(4):
                vx = ux + fx[k]
                vy = uy + fy[k]
                
                if 0 <= vx < m and 0 <= vy < n and rooms[vx][vy] == INF:
                    rooms[vx][vy] = rooms[ux][uy] + 1
                    q.append((vx, vy))
        