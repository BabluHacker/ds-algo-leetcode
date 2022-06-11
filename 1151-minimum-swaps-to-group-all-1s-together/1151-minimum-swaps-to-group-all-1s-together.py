class Solution:
    def minSwaps(self, data: List[int]) -> int:
        window = 0
        for i in data:
            if i == 1:
                window += 1
        
        one = 0
        l, r = 0, 0 
        max_one = 0
        while r<len(data):
            if data[r] == 1:
                one += 1
            
            if r+1 >= window:
                max_one = max(max_one, one)
                if data[l] == 1:
                    one -= 1
                l+=1
            
            r += 1
            
        return window - max_one
            
        