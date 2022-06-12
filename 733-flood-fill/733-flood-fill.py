class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        ROW, COL = len(image), len(image[0])
        q = []
        old_col = image[sr][sc]
        if old_col == newColor: return image
        q.append((sr,sc))
        
        
        
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        while q:
            
            r, c = q.pop(0)
            image[r][c] = newColor
            for i in range(4):
                nr, nc = r+dx[i], c+dy[i]
                if 0<=nr<ROW and 0<=nc<COL and image[nr][nc] == old_col:
                    q.append((nr,nc))
        return image
                
        
        