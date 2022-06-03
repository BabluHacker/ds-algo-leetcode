class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sub_box = [[set() for _ in range(3)] for _ in range(3)]
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)] 
        # print(row)
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != ".":
                    # add 3x3
                    sub_r = i//3
                    sub_c = j//3
                    
                    if board[i][j] in sub_box[sub_r][sub_c]:
                        # print(0, i, j)
                        
                        return False
                    sub_box[sub_r][sub_c].add(board[i][j])
                    
                    # row wise add
                    if board[i][j] in row[i]:
                        # print(row)
                        # print(1, i, j)
                        return False
                    row[i].add(board[i][j])
                    
                    # col wise add
                    if board[i][j] in col[j]:
                        # print(2, i, j)
                        return False
                    col[j].add(board[i][j])
        
        
        return True