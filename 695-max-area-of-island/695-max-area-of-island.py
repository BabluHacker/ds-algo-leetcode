class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROW, COL = len(grid), len(grid[0])
        
        visited = set()
        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROW or c >= COL or (r,c) in visited or grid[r][c] == 0:
                return
            
            visited.add((r,c))
            
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            
        max_area = 0
        prev_total_area = 0
        for r in range(ROW):
            for c in range(COL):
                if (r,c) not in visited and grid[r][c] == 1:
                    dfs(r,c)
                    # update max area
                    # print(len(visited), prev_total_area, max_area, r, c)
                    
                    max_area = max(max_area, len(visited)-prev_total_area)
                    prev_total_area = len(visited)
        return max_area