class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        island = 0
        seen = set()
        
        def dfs(r,c):
            if r<0 or c<0 or r>=ROW or c>=COL or grid[r][c] == 0 or (r,c) in seen:
                return
            
            
            seen.add((r, c))
            current_island.add((r-r_origin, c-c_origin))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            
            return 
            
            
        
        unique_island = set()
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] and (r,c) not in seen:
                    current_island = set()
                    r_origin, c_origin = r, c
                    dfs(r,c)
                    unique_island.add(frozenset(current_island))
        return len(unique_island)