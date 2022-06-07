  
class Solution:
    def __init__(self):
        self.g = defaultdict(list)
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        for pre in prerequisites:
            self.g[pre[0]].append(pre[1])
        
        
        def has_cycle(crs, visit, recstack): # if cycle found then return True
            visit.add(crs)
            recstack.add(crs)
            
            for nei in self.g[crs]:
                if nei not in visit:
                    if has_cycle(nei, visit, recstack) == True:
                        return True
                elif nei in recstack:
                    return True
            recstack.remove(crs)
            return False
        
        visit, recstack = set(), set()
        for i in range(numCourses):
            if has_cycle(i, visit, recstack) == True:
                return False # can't complete the course as there is a cycle 
        return True 
            
            
        
        