class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        maxlen = 1
        start = 0
        low = 0
        high = 0
        for i in range(1, l):
            # for odd palindrome
            low = i-1
            high = i+1
            while low >=0 and high < l and s[low] == s[high]:
                low -= 1
                high += 1
            low += 1
            high -= 1
            if maxlen < (high-low+1):
                maxlen = (high-low+1)
                start = low
            
            # for even palindrome
            low = i-1
            high = i
            while low >= 0 and high < l and s[low] == s[high]:
                low -= 1
                high += 1
            low += 1
            high -= 1
            if maxlen < (high-low+1):
                maxlen = (high-low+1)
                start = low
        
        return s[start:start+maxlen]
        