class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        storage = {}
        res = []
        for i in range(len(nums)):
            if target-nums[i] in storage:
                res = [storage[target-nums[i]], i]
                break
            
            storage[nums[i]] = i
        return res