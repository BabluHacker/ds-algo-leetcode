class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1: return len(s)
        pos = {}
        st = 0
        start = 0
        max_len = 0 
        for i in range(0, len(s)):
            if s[i] in pos:
                if pos[s[i]] >= st: # inside the current sub str
                    curr_len = i-st
                    if curr_len > max_len:
                        max_len = curr_len
                        start = st
                    st = pos[s[i]] + 1
            pos[s[i]] = i
            
        curr_len = i-st+1
        if curr_len > max_len:
            max_len = curr_len
            start = st
        return max_len
                    