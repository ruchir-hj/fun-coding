class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        self.combineHelper(n, k, 1, result, [])
        return result

    def combineHelper(self, n, k, start, result, cur):
        if k == 0:
            result.append(cur[:])
            return

        for i in xrange(start, n + 1):
            cur.append(i)
            self.combineHelper(n, k - 1, i + 1, result, cur)
            cur.pop()