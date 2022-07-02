class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        char_occur = False
        l = 0
        for char in reversed(s):
            if char == ' ' and not char_occur:
                continue
            else:
                char_occur = True
            if char_occur:
                if char == ' ':
                    return l
                l += 1
        
        return l
            