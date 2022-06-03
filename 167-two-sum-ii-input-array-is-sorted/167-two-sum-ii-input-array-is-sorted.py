class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp = {}
        
        for i in range(len(numbers)):
            if target - numbers[i] in mp:
                first = target - numbers[i]
                
                return [mp[first]+1, i+1]
            mp[numbers[i]] = i
        
            
        