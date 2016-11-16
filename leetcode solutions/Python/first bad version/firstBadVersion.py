# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) / 2
            if isBadVersion(mid) and (mid - 1 < 0 or not isBadVersion(mid - 1)):
                return mid
            elif isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1