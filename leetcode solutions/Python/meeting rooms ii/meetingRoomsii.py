# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        starts, ends = [], []
        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)

        starts.sort()
        ends.sort()

        s, e = 0, 0
        min_rooms, cnt_rooms = 0,0

        while s < len(starts):
            if starts[s] < ends[e]:
                cnt_rooms += 1
                min_rooms = max(min_rooms, cnt_rooms)
                s += 1
            else:
                cnt_rooms -= 1
                e += 1

        return min_rooms
