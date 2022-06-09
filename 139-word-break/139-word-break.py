class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        dp[len(s)] = True
        def segment(s, i):
            if i in dp: return dp[i]
            if i == len(s): return True
            elif i > len(s): return False
            for word in wordDict:
                if s[i:i+len(word)] == word:
                    if segment(s, i+len(word)):
                        dp[i] = True
                        return dp[i]
            dp[i] = False
            return dp[i]
        
        return segment(s, 0)
                