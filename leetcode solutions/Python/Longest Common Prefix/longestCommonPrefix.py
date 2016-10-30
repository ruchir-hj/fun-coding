class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        for i in xrange(0, len(strs[0])):
            for currString in strs[1:]:
                if i >= len(currString) or currString[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]



