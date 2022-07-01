class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums = sorted(nums)
        
        l, r = 0, len(nums)-1
        steps = 0
        
        while l<r:
            steps += (nums[r] - nums[l])
            l += 1
            r -= 1
        return steps