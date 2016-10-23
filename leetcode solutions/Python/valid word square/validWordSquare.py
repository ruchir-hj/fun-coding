class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        if not words:
            return True

        for i in xrange(0, len(words)):
            for j in xrange(0, len(words[i])):
                if j >= len(words) or len(words[j]) <= i or words[i][j] != words[j][i]:
                    return False

        return True

