class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visit = set()
        
        ROW, COL = len(board), len(board[0])
        
        dx = [-1,1,0,0]
        dy = [0,0,1,-1]
                    
                
        def dfs(r,c, capture=False):
            if r<0 or c<0 or r>=ROW or c>=COL or (r,c) in visit or board[r][c] == "X":
                return
            visit.add((r,c))
            if capture:
                board[r][c] = "X"
            dfs(r-1,c, capture)
            dfs(r+1,c, capture)
            dfs(r,c-1, capture)
            dfs(r,c+1, capture)
        
        # visit un captured cells
        for r in range(ROW):
            dfs(r, 0)
            dfs(r, COL-1)
        for c in range(COL):
            dfs(0, c)
            dfs(ROW-1, c)
        
        # print(visit)
            
        # visit captured cells
        for r in range(1, ROW-1):
            for c in range(1, COL-1):
                if (r,c) not in visit and board[r][c] == "O":
                    # dfs(r,c, True)
                    board[r][c] = "X"
        
                    
        
        return board
    
        