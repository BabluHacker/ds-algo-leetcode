class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix), len(matrix[0])
        # print('test', ROW, COL)
        l, r = 0, ROW*COL-1
        
        while l <= r:
            m = l + (r-l)//2
            
            new_r, new_c = int(m) // COL, m%COL
            
            # print(new_r, new_c)
            if matrix[new_r][new_c] == target:
                return True
            elif matrix[new_r][new_c] < target:
                l = m+1
            else:
                r = m-1
        return False
    