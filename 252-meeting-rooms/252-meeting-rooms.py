class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals: return True
        intervals.sort()
        # print(intervals)
        start, end = intervals[0]
        for s, e in intervals[1:]:
            if s < end:
                return False
            end = e
                
        return True
                