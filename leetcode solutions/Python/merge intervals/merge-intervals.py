# Defination for an interval
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return intervals

        intervals.sort(key = lambda x : x.start)
        result = [intervals[0]]

        for i in range(1, len(intervals)):
            prev, current = result[-1], intervals[i]

            if current.start <= prev.end:
                prev.end = max(prev.end, current.end)
            else:
                result.append(current)

        return result