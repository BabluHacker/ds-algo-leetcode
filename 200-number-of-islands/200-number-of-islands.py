class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def bfs( r, c):
            

            queue = [(r,c)]
            grid[r][c] = "-1"

            dx = [0, 0, -1, 1]
            dy = [1, -1, 0, 0]

            ROW = len(grid)
            COL = len(grid[0])

            while queue:
                n = queue.pop(0)
                

                for i in range(4):
                    new_i = n[0] + dx[i]
                    new_j = n[1] + dy[i]
                    
                    if new_i>=0 and new_j>=0 and new_i<ROW and new_j<COL:
                        if grid[new_i][new_j] != "-1" and grid[new_i][new_j] == "1":
                            queue.append((new_i, new_j))
                            grid[new_i][new_j] = -1


        island = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                
                if grid[i][j] == "1":
                 
                    island += 1
                    bfs(i, j)
      
        return island
                