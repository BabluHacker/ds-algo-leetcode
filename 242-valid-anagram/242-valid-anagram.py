class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        mp = {}
        
        for i in range(len(s)):
            mp[s[i]] = 1 + mp.get(s[i], 0)
        
        for i in range(len(t)):
            mp[t[i]] = mp.get(t[i], 0) - 1
            if mp[t[i]] < 0:
                return False
        
        for key, value in mp.items():
            if value != 0:
                return False
        return True