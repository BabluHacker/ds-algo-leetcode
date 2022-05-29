from collections import Counter
class Solution:
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ## APproach heap - using Collections library
        
        #count = Counter(nums)
        #
        #return heapq.nlargest(k, count.keys(), key = lambda g: count.get(g))
    
    
    
    
        # twicked bucket sort algo
        
        # 1. find the occurences
        # 2. create the bucket by putting the count as index and elements are the value
        # 3. iterate reversed to find top k items
        
        n = len(nums)
        mp = {}
        for i in nums:
            mp[i] = 1 + mp.get(i, 0)
        
        # create the bucket
        bucket = [set() for _ in range(n+1)]
        for value in mp.keys():
            bucket[mp[value]].add(value)
        print(bucket)
        
        # iterate reversely to get top k 
        result = []
        for elements in reversed(bucket):
            if elements:
                l = list(elements)
                result.extend(l)
                k -= len(l)
            if k <= 0:
                break
                
        if k < 0:
            return result[0:k]
        return result
        
        
        
        
        
        
        
        