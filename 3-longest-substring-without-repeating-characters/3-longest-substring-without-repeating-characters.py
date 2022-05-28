class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1: return len(s)
        start = 0 # starting index of resulted substring
        st = 0 # starting index of current substring 
        pos = {}
        pos[s[0]] = 0 # first char position is 0
        maxlen = 0
        for i in range(1, len(s)):
            if s[i] in pos: # already visited
                if pos[s[i]] >= st: # stored position is still inside current substring
                    currlen = i - st
                    if currlen > maxlen:
                        maxlen = currlen
                        start = st # store current substring result to start before breaking it
                    st = pos[s[i]] + 1 # update st with visited last position+1
            pos[s[i]] = i # always update lated visited position
            # print(maxlen)
        # calculate last substring len 
        print(i)
        currlen = i - st + 1
        # print(i-st)
        if currlen > maxlen:
            maxlen = currlen
            start = st
        # print(s[start:start+maxlen])
        return maxlen
        