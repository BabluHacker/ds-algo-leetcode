class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n <= 2: return []
        
        nums = sorted(nums)
        result = []
        for i in range(n-2):
            two_sums = self.twoSum(nums, i+1, n-1, -nums[i])
            if len(two_sums) > 0:
                for sums in two_sums:
                    dummy = sums + [nums[i]]
                    if dummy not in result:
                        result.append(dummy)

        return result 
        
    def twoSum(self, nums, start, end, target):
        result = []
        while start < end:
            if nums[start] + nums[end] == target:
                result.append([nums[start], nums[end]])
                start += 1
                end -= 1
            elif nums[start] + nums[end] < target:
                start += 1
            else:
                end -= 1
        return result
        