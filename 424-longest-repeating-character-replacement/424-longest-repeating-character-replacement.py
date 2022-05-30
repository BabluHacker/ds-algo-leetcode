class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #### O (n) solution
        n = len(s)
        counter = {}
        max_f = 0
        l = 0
        res = 0
        
        # iterate right 
        for r in range(n):
            counter[s[r]] = 1 + counter.get(s[r], 0)
            max_f = max(max_f, counter[s[r]]) # update max_f when right is moved
            
            while ((r-l+1)-max_f > k): # if swap needs > k then move left pointer
                counter[s[l]] -= 1
                l += 1
                
                # no need to update max_f because if count is decreasing and decreasing counter can't impact on (r-l+1)-max_f <= k condition. here max_f needs to bigger to get res updated. but while left is moving then counter -= 1, so max_f will be minimum
            
            # loop breaks while there is a minimum/equal swap then k 
            res = max(res, (r-l+1))
        return res
        
        
        
        
        
        
        
        #### O (26*n)
        
        
        
#         n = len(s)
#         if n <= k: return n
#         start, end = 0, 0
#         counter = {}
#         max_size = 0
#         counter[s[start]] = 1 + counter.get(s[start], 0)
#         while(start<n and end<n):
            
#             curr_window = end - start + 1
#             max_freq = self.get_max_freq(counter)
#             # print(start, end, curr_window, max_freq, counter)
#             if curr_window - max_freq <= k:
#                 max_size = max(max_size, curr_window)
#                 # move end 
#                 end += 1
#                 if end < n: 
#                     counter[s[end]] = 1 + counter.get(s[end], 0)
#             else: # exceeds k swap, so, need to move start
#                 counter[s[start]] -= 1
#                 start += 1
                
#             # print(start, end)
#         return max_size
            
            
#     def get_max_freq(self, counter):
#         max_f = 0
#         for i in counter.keys():
#             max_f = max(max_f, counter[i])
#         return max_f
                
        
        
"""
AABABBA, k = 2
start, end , curr_window, max_f, max_size, string
0,      0,      1,          1(A),      1,       A
0,      1       2           2(A)       2        AA
0,      2,      3           2(A)       3        AAB (swap 1 < k)
0,      3,      4           3(A)       4        ,AABA(swap 2 < k)





"""