class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        n = len(s)
        dp[n] = 1 # base case, 
        def countWays(i):
            if i in dp: return dp[i]
            
            if s[i] == "0" : return 0
            
            if i not in dp:
                res = countWays(i+1) # s[i] is not 0 that's why i+1 may have result
                if (i+1 < n and (s[i]=="1" or (s[i]=="2" and s[i+1] in "0123456"))):
                    # taking 2 digit here, between 10~26
                    res += countWays(i+2)
                dp[i] = res
            return dp[i]
            
        return countWays(0)