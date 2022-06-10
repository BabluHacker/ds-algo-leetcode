class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]
        result = []
        sorted_strs = []
        for s in strs:
            sorted_strs.append(''.join(sorted(s)))
        
        print(sorted_strs)
        
        mp = {} # store the original values of anagram
        
        for i in range(len(sorted_strs)):
            if sorted_strs[i] in mp:
                mp[sorted_strs[i]].append(strs[i])
            else:
                mp[sorted_strs[i]] = [strs[i]]
        # print(mp)
        
        for i in mp.keys():
            result.append(mp[i])
        return result
            
            
        