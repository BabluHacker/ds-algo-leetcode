class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        n = len(s)
        i = 0
        while i<n:
            print(i)
            if i < n-1 and values[s[i]] < values[s[i+1]]:
                total += (values[s[i+1]] - values[s[i]])
                i += 1
            else:
                total += values[s[i]]
            i += 1
        return total