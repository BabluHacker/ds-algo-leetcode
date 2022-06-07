class Solution:
    def rob(self, nums: List[int]) -> int:
        rob = {}
        n = len(nums)
        rob[n], rob[n+1] = 0, 0
        
        def getAmount(i):
            if i not in rob:
                rob[i] = max(getAmount(i+1), nums[i]+getAmount(i+2))
            return rob[i]
        
        return getAmount(0)