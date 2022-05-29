class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s  = ''
        for i, char in enumerate(s):
            char = char.lower() 
            if (char >= 'a' and char <= 'z') or (char >= '0' and char <= '9'):
                new_s += char
            else:
                continue
        new_len = len(new_s)
        k = new_len // 2
        for i in range(0, k):
            if new_s[i] != new_s[new_len - i - 1]:
                return False
        return True
        