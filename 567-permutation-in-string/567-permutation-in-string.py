class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mp_s1 = {}
        mp_s2 = {}
        n = len(s1)
        # creating the hashmap for s1
        for i in range(len(s1)):
            mp_s1[s1[i]] = 1 + mp_s1.get(s1[i], 0)
        
            
        # for every sub string find hashmap
        for i in range(len(s2)-n+1):
            
            if self.match(mp_s1.copy(), s2[i:i+n]):
                # exists
                return True
        return False
            
        
    def match(self, ms1, sub_str):
        # print(sub_str, ms1)
        for s in sub_str:
            if s in ms1:
                ms1[s] -= 1
            else:
                return False
        for v in ms1.items():
            if v[1] != 0:
                return False
        return True
            