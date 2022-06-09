class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posDiag = set() # (r-c)
        negDiag = set() # (r+c)
        
        board = [["."]*n for _ in range(n)]
        res = []
        def backtrack(r):
            if r == n:
                copy = ["".join(b) for b in board]
                res.append(copy)
                return 
        
            for c in range(n):
                if c in cols or (r+c) in negDiag or (r-c) in posDiag:
                    continue
                
                board[r][c] ="Q"
                cols.add(c)
                posDiag.add(r-c)
                negDiag.add(r+c)
                
                backtrack(r+1)
                
                board[r][c] = "."
                cols.remove(c)
                posDiag.remove(r-c)
                negDiag.remove(r+c)
                
        backtrack(0)
        return res
                
                