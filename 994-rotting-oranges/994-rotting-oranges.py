class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        ROW, COL = len(grid), len(grid[0])
        q = []
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        time = 0
        while q:
            
            curr_len = len(q)
            for j in range(curr_len):
                r, c = q.pop(0)

                for i in range(4):
                    nr, nc = r+dx[i], c+dy[i]
                    if 0<=nr<ROW and 0<=nc<COL and grid[nr][nc] == 1:
                        grid[nr][nc] += 1
                        q.append((nr,nc))
                        fresh -= 1
            time += 1
            
        time = time-1 if time > 0 else 0
        return time if fresh==0 else -1