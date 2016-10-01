class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        colNum = 0
        count = 0

        for i in xrange(0, len(s)):
            colNum = colNum * 26 + (ord(s[i]) - ord('A') + 1)

        return colNum