class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mp = {}
        hasDup = False
        for i in range(len(nums)):
            if nums[i] in mp:
                hasDup = True
                break
            mp[nums[i]] = 1
        return hasDup
        