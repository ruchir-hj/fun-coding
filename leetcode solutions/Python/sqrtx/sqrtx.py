class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        left = 0
        right = x/2

        while left <= right:
            mid = left + (right - left)/2
            n = mid * mid
            if n == x:
                return mid
            elif n > x:
                right = mid - 1
            else:
                left = mid + 1

        return right
