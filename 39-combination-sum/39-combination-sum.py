class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 2 decision-> 1. use the same , 2. not use the same
        
        res = []
        
        def dfs(i, curr, total):
            if total > target: return
            if i >= len(candidates): return
            
            if target == total:
                res.append(curr.copy())
                return
            # 1st decision: using same value
            curr.append(candidates[i])
            dfs(i, curr, total+candidates[i])
            
            # 2nd decision: not using same value
            curr.pop()
            dfs(i+1, curr, total)
            
            return 
        
        dfs(0, [], 0)
        return res