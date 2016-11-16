class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if not s or not wordDict:
            return False

        can_break = [False for _ in xrange(len(s) + 1)]
        can_break[0] = True
        max_len = 0

        for word in wordDict:
            max_len = max(max_len, len(word))

        for i in xrange(0, len(s) + 1):
            for j in xrange(0, min(i, max_len) + 1):
                if can_break[i - j] == True and s[i - j:i] in wordDict:
                    can_break[i] = True
                    break

        return can_break[-1]





