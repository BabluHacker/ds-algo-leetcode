class Solution:
    def __init__(self):
        self.g = defaultdict(list)
        self.ans = []
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        for pre in prerequisites:
            self.g[pre[0]].append(pre[1])
            
        visit, recstack = set(), set()
        def has_cycle(crs):
            
            visit.add(crs)
            recstack.add(crs)
            
            for nei in self.g[crs]:
                if nei not in visit:
                    if has_cycle(nei) == True:
                        return True
                elif nei in recstack: # there is a cyle
                    return True
                
            self.ans.append(crs)
            recstack.remove(crs)
            return False
                
        
        for i in range(numCourses):
            if i not in visit:
                if has_cycle(i) == True:
                    return []
            
                
        return self.ans 