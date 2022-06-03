class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ## 1st approach
        
#         mp = {}
        
#         for i in range(len(numbers)):
#             if target - numbers[i] in mp:
#                 first = target - numbers[i]
                
#                 return [mp[first]+1, i+1]
#             mp[numbers[i]] = i
        
#         return -1
        
    
        ## 2nd approach
        s = 0
        p1, p2 = 0, len(numbers)-1
        
        while p1 < p2:
            curr_sum = numbers[p1] + numbers[p2]
            if curr_sum == target:
                return [p1+1, p2+1]
            if curr_sum > target:
                p2 -= 1
            else:
                p1 += 1
        return -1