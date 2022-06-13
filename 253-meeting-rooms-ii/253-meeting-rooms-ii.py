class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda k:k[0])
        rooms = 0
        print(intervals)
        
        processing_endtime = []
        for timing in intervals:
            assigned = False
            for endtime in processing_endtime:
                if endtime <= timing[0] : # new meeting start time is later than a                                               #ended meeting. so just pop out that                                                #meeting and assign to this meeting
                    assigned= True
                    processing_endtime.remove(endtime)
                    processing_endtime.append(timing[1])
                    break
            
            if not assigned:
                rooms += 1
                processing_endtime.append(timing[1])
        return rooms
            
                