# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """

        if len(intervals) == 1:
            return True

        intervals.sort(key = lambda x : x.start)

        for i in range(0, len(intervals) - 1):
            if intervals[i].end > intervals[i + 1].start:
                return False

        return True

