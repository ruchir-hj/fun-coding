class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        res = []
        for d in num:
            while k and res and res[-1] > d:
                res.pop()
                k -= 1

            res.append(d)

        return ''.join(res).lstrip('0')[:-k or None] or '0'
