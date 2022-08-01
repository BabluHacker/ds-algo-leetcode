class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]
        # sort strs
        sorted_strs = []
        for i in range(len(strs)):
            sorted_strs.append(''.join(sorted(strs[i])))
        
        mp = {}
        
        for i in range(len(strs)):
            if sorted_strs[i] in mp:
                mp[sorted_strs[i]].append(strs[i])
            else:
                mp[sorted_strs[i]] = [strs[i]]
        
        result = []
        for key, value in mp.items():
            result.append(value)
        
        return result