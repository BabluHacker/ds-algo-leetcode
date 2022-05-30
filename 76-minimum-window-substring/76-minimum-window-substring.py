class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have = {}
        need = {}
        need_cond, have_cond = 0, 0
        next_start_i = []
        
        # creating need hash_map
        for i in range(len(t)):
            need[t[i]] = 1 + need.get(t[i], 0)
        need_cond = len(need)
        
        l = 0
        min_window = sys.maxsize 
        output = []
        
        for r in range(len(s)):
            if s[r] in need:
                have[s[r]] = 1 + have.get(s[r], 0)
                if have[s[r]] == need[s[r]]:
                    have_cond += 1

            while have_cond == need_cond:
                if r-l+1 < min_window:
                    min_window = r-l+1
                    output = [l,r]
                if s[l] in have:
                    have[s[l]] -= 1
                    if have[s[l]] < need[s[l]]: have_cond -= 1
                l += 1
        if not output: return ""
        return s[output[0]:output[1]+1]
                    
                
        
        
        