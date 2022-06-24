class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        for i in range(len(arr)):
            freq[arr[i]] = 1 + freq.get(arr[i], 0)
        
        bucket = {}
        
        for key, f in freq.items():
            if f in bucket:
                return False
            bucket[f] = key
        return True