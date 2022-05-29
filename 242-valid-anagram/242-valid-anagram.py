class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        mp = {}
        # calculating the char counts
        for ch in s:
            if ch in mp:
                mp[ch] += 1
            else:
                mp[ch] = 1
                
        for ch in t:
            if ch not in mp:
                return False # if not in mp then not a anagram
            else:
                mp[ch] -= 1
                if mp[ch] < 0: return False # if any char is extra here then False
        
        # check the mp if any char count is != 0
        for i in mp.keys():
            if mp[i] != 0:
                return False
        return True
                
        