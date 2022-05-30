class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        if n <= k: return n
        start, end = 0, 0
        counter = {}
        max_size = 0
        counter[s[start]] = 1 + counter.get(s[start], 0)
        while(start<n and end<n):
            
            curr_window = end - start + 1
            max_freq = self.get_max_freq(counter)
            # print(start, end, curr_window, max_freq, counter)
            if curr_window - max_freq <= k:
                max_size = max(max_size, curr_window)
                # move end 
                end += 1
                if end < n: 
                    counter[s[end]] = 1 + counter.get(s[end], 0)
            else: # exceeds k swap, so, need to move start
                counter[s[start]] -= 1
                start += 1
                
            # print(start, end)
        return max_size
            
            
    def get_max_freq(self, counter):
        max_f = 0
        for i in counter.keys():
            max_f = max(max_f, counter[i])
        return max_f
                
        
        
"""
AABABBA, k = 2
start, end , curr_window, max_f, max_size, string
0,      0,      1,          1(A),      1,       A
0,      1       2           2(A)       2        AA
0,      2,      3           2(A)       3        AAB (swap 1 < k)
0,      3,      4           3(A)       4        ,AABA(swap 2 < k)





"""