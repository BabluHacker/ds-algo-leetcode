class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for i in range(len(intervals)):
            # newInterval is not overlapping to current and happening before
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:] 
            elif intervals[i][1] < newInterval[0]: # not overlapping till now, happening later
                res.append(intervals[i])
            else: # overlapping and merge to newIntervals
                # print("1", intervals[i], newInterval)
                newInterval = [min(newInterval[0],intervals[i][0]), max(newInterval[1],intervals[i][1])]
            # print(newInterval)
        res.append(newInterval)
        return res