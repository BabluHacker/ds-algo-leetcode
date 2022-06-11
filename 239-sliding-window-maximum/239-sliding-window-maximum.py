class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # monotonically decreasing queue
        n = len(nums)
        if n * k == 0: return []
        if k == 1: return nums
        
        q = collections.deque()
        l = r = 0
        res = []
        while r<n:
            
            # from the right pop which values are less than nums[r] bcz it has to be decreasing
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            if l > q[0]: # as q[0] is max and l is moving then just pop left max value
                q.popleft()
                
            if (r+1) >= k:
                res.append(nums[q[0]])
                l += 1 # moving window
            r += 1
            # print(q, res)
        return res
            
            
        