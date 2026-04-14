"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([x.start for x in intervals])
        ends = sorted([x.end for x in intervals])
        
        res = rooms = 0
        s = e = 0

        while s < len(intervals):
            if starts[s] < ends[e]:
                rooms +=1
                s += 1
            else:
                e += 1
                rooms-=1
            
            res = max(rooms, res)

        return res
