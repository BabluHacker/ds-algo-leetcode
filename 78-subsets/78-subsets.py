class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        subset = []
        def find(i):
            if i >= n: 
                res.append(subset.copy())
                return 
            subset.append(nums[i])
            find(i+1)
            
            subset.pop()
            find(i+1)
        find(0)
        return res
            