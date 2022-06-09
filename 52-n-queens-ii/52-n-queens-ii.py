class Solution:
    def __init__(self):
        self.ans = 0
    def totalNQueens(self, n: int) -> int:
        cols = set()
        posDiag = set() # (r-c)
        negDiag = set() # (r+c)
        
        
        def backtrack(r):
            
            if r == n:
                self.ans += 1
                return 
            
            for c in range(n):
                if c in cols or (r+c) in negDiag or (r-c) in posDiag:
                    continue
                    
                cols.add(c)
                posDiag.add(r-c)
                negDiag.add(r+c)
                
                backtrack(r+1)
                
                cols.remove(c)
                posDiag.remove(r-c)
                negDiag.remove(r+c)
                
        
        backtrack(0)
        return self.ans
                    