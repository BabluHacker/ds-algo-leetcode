class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # if overlapped just delete (hypthetically) the max(both ends), so update prevEnd to min(both end) ignor the deleted interval
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if prevEnd <= start: # not overlapping
                prevEnd = end
            else: # overlapped, delete the max end's interval
                res += 1
                prevEnd = min(end, prevEnd)
        return res
                
        