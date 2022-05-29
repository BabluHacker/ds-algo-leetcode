class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1]*n
        
        for i in range(1, n):    
            result[i] = result[i-1] * nums[i-1]
        print(result)
        # backward iteration
        curr = 1
        for i in reversed(range(n)):
            
            result[i] = result[i] * curr 
            curr *= nums[i]
        
        return result