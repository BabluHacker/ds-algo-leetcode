class Solution:
    def __init__(self):
        self.g = defaultdict(list)
        
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        for e in edges:
            self.g[e[0]].append(e[1])
            self.g[e[1]].append(e[0])
            
        visit = set()
        def dfs(node):
            visit.add(node)
            
            for nei in self.g[node]:
                if nei not in visit:
                    dfs(nei)
        counter = 0
        for i in range(n):
            if i not in visit:
                dfs(i)
                counter += 1
        return counter