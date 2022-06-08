class Solution:
    def countSubstrings(self, s: str) -> int:
        res = [n for n in s]
        start = 0
        l = len(s)
        low, high = 0, 0
        for i in range(1, l):
            low = i - 1
            high = i + 1
            while low >= 0 and high < l and s[low] == s[high]:
                res.append(s[low:high+1])
                low -= 1
                high += 1
            low = i-1
            high = i
            while low >=0 and high < l and s[low] == s[high]:
                res.append(s[low:high+1])
                low -= 1
                high += 1
        # print(res)
        return len(res)
            
        