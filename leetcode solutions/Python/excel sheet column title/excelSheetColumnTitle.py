class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = []
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        while n > 0:
            res.append(capitals[(n - 1) % 26])
            n = (n - 1) // 26
        res.reverse()
        return ''.join(res)

