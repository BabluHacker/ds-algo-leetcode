class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        res = []
        l, r = 0, len(nums)-1
        while len(nums) != len(res):
            res.append(nums[l])
            l += 1
            
            if l < r:
                res.append(nums[r])
                r -= 1
        return res