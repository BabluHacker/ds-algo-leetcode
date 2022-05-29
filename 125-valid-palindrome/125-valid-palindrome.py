class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1, p2 = 0, len(s)-1
        isPalin = True
        while p1 < p2:
            if not self.isAlphaNumeric(s[p1]):
                p1 += 1
                continue
            if not self.isAlphaNumeric(s[p2]):
                p2 -= 1
                continue
            
            if s[p1].lower() != s[p2].lower():
                # print(p1, p2)
                isPalin = False
                break
            p1 += 1
            p2 -= 1
        
        return isPalin
    def isAlphaNumeric(self, char):
        if (char >= 'a' and char <= 'z') or (char >= '0' and char <= '9') or (char >= 'A' and char <= 'Z'):
            return True
        return False
            