class Solution:
    def __init__(self):
        self.g = defaultdict(list)
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        for e in edges:
            self.g[e[0]].append(e[1])
            self.g[e[1]].append(e[0])
        
        visit = set()
        
        def has_cycle(node, parent):
            
            visit.add(node)
            
            for nei in self.g[node]:
                if nei not in visit:
                    if has_cycle(nei, node) == True:
                        return True
                elif parent != nei:
                    return True
            return False
        
        counter_disjoint = 0
        for i in range(n):
            if i not in visit:
                counter_disjoint += 1
                
                if has_cycle(i, -1) == True or counter_disjoint > 1:
                    return False # not a valid tree
                
        return True
        
            