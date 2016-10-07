import collections

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        strLst = str.split(" ")

        if len(pattern) != len(strLst):
            return False


        indexMap1 = collections.defaultdict(list)
        indexMap2 = collections.defaultdict(list)

        for i in xrange(0, len(pattern)):
            indexMap1[strLst[i]].append(i)
            indexMap2[pattern[i]].append(i)

            if indexMap1[strLst[i]] != indexMap2[pattern[i]]:
                return False

        return True