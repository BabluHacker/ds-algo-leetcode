class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count, prev, curr, n = 0, 0, 1, len(s)
        for i in range(1, n):
            if s[i-1] != s[i]: # digit changed, store occurrences
                count += min(prev, curr)
                prev, curr = curr, 1 # reset curr
            else:
                curr += 1 # storing any current digit occurences
        
        count += min(curr, prev)
        return count
            