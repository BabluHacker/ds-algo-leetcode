class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        processing_endtime = []
        rooms = 0
        for start, end in intervals:
            replaced = False
            for p_end in processing_endtime:
                if p_end <= start: # replace the room
                    processing_endtime.remove(p_end)
                    processing_endtime.append(end)
                    replaced = True
                    break
                    
            if not replaced: # new room allocated
                rooms += 1
                processing_endtime.append(end)
            
        return rooms
        