class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(nlogn) solution
        
#         if not nums:
#             return 0
#         nums = list(sorted(set(nums)))
#         # print(nums)
        
#         count = 1
#         max_count = 0
#         print(nums)
#         for i in range(1, len(nums)):
#             if nums[i] - nums[i-1] == 1:
#                 count += 1
#             else:
#                 max_count = max(max_count, count)
#                 count = 1
#         return max(max_count, count)


######## O(n) solution
        
    # store all the elm in a set
    # iterate over set and for every elm in set do this
        # check if s is the first elm of sub_set byt checking s-1 is in the set
        # if s-1 not in set: then get count of full sub_set  and store max of that
        # if s-1 in set: then nothing 
        
        nums_set = set(nums)
        max_size = 0
        
        for i in nums_set:
            if i-1 not in nums_set: # i is the first value of a sub_array 
                curr = i+1
                count = 1
                while curr in nums_set:
                    count += 1
                    curr += 1
                max_size = max(max_size, count)
        return max_size
                    
                    
        