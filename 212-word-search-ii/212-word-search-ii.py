class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Solution:
    def __init__(self):
        self.ans = set()
        self.root = TrieNode()
        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # construct Trie from the words
        for word in words:
            self.construct(word)
        
        
        lw = len(words)
        # DSF
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        ROW, COL = len(board), len(board[0])
        visit = set()
        def dfs(r, c, node, word):
            if (r<0 or c<0 or r==ROW or c==COL or (r,c) in visit 
                or board[r][c] not in node.children or len(self.ans) == lw):
                return 
            
            
            visit.add((r,c))
            
            ch = board[r][c]
            node = node.children[ch]
            
            word += ch
            if node.word:
                self.ans.add(word)
                
            #4 diretional dfs
            for i in range(4):
                dfs(r+dx[i], c+dy[i], node, word)
                
            # bcs word can be found by backtracking.
            visit.remove((r,c))
            
        
        # ietrate over board, for every char run dfs
        for i in range(ROW):
            for j in range(COL):
                if len(self.ans) != lw:
                    dfs(i, j, self.root, "")
        return list(self.ans)
    
    
    
    
    def construct(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True