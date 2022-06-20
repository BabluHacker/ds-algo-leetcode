class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROW, COL = len(matrix), len(matrix[0])
        dp = [[-sys.maxsize]*COL for _ in range(ROW)]
        
        def dfs(r, c, prev):
            
            if r<0 or c<0 or r>=ROW or c>=COL or matrix[r][c] <= prev:
                return 0
            if dp[r][c] > 0:
                return dp[r][c]
            
            dp[r][c] = max(dp[r][c], 1+dfs(r+1, c, matrix[r][c]))
            dp[r][c] = max(dp[r][c], 1+dfs(r-1, c, matrix[r][c]))
            dp[r][c] = max(dp[r][c], 1+dfs(r, c+1, matrix[r][c]))
            dp[r][c] = max(dp[r][c], 1+dfs(r, c-1, matrix[r][c]))
            
            return dp[r][c]
        
        ans = 0
        for r in range(ROW):
            for c in range(COL):
                ans = max(ans, dfs(r, c, -sys.maxsize))
                # print(dp)
        return ans