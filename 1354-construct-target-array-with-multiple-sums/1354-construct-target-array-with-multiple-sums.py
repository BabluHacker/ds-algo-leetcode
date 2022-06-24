class Solution:
    def isPossible(self, target: List[int]) -> bool:
        # going backward to find all 1's
        n = len(target)
        if n == 1: 
            return target[0] == 1
        
        # for n>=2
        pq = [-num for num in target]
        heapq.heapify(pq)
        
        total_sum = sum(target)
        while -pq[0] > 1:
            largest = -pq[0]
            # give TLE for [1,2,10000000] where largest is more larger than other sum. here
            # x = largest - (total_sum - largest)
            # if x < 1:
            #     return False
         
            
            
            # better approach
            rest = total_sum - largest
            if rest == 1:
                return True
            x = largest % rest
            if x == 0 or x == largest:
                return False
            
            heapq.heappop(pq)
            heapq.heappush(pq, -x)
            total_sum = total_sum - largest + x
            
        return True