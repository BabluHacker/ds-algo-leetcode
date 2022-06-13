class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda k: k[0])
        start = intervals[0][0]
        end = intervals[0][1]
        result = []
        for i in range(0, len(intervals)):
            # print(start, end, intervals[i])
            if end < intervals[i][0]: # new start , distinct range
                result.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
            else: # overlapped start, update end
                if end < intervals[i][1]:
                    end = intervals[i][1]
                # else nothing, old end is the new end
        
        # append last start and end
        result.append([start, end])
        return result
        