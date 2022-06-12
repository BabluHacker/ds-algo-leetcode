class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        ROW, COL = len(rooms), len(rooms[0])
        GATE = 0
        EMPTY = 2147483647
        q = []
        for r in range(ROW):
            for c in range(COL):
                if rooms[r][c] == GATE:
                    q.append((r,c))
        
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        while q:
            r, c = q.pop(0)
            for i in range(4):
                nr, nc = r+dx[i], c+dy[i]
                if 0<=nr<ROW and 0<=nc<COL and rooms[nr][nc] == EMPTY:
                    rooms[nr][nc] = 1 + rooms[r][c]
                    q.append((nr, nc))
        
        