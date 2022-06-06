class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
    
    def addword(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True
        
            
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        root = TrieNode()
        root.addword(word)
        
        res, visited = set(), set()
        ROW, COL = len(board), len(board[0])
        
        def dfs(i, j, word, node):
            if (i < 0 or j < 0 or i == ROW or j == COL 
                or board[i][j] not in node.children 
                or (i,j) in visited):
                return 
            
            visited.add((i,j))
            ch = board[i][j]
            
            word += ch
            node = node.children[ch]
            if node.word:
                res.add(word)
                return 
            
            dfs(i+1, j, word, node)
            dfs(i-1, j, word, node)
            dfs(i, j+1, word, node)
            dfs(i, j-1, word, node)
            
            visited.remove((i,j))
            
        for r in range(ROW):
            for c in range(COL):
                dfs(r, c, "", root)
        if len(res) > 0: return True
        return False
            
            
            
            
            