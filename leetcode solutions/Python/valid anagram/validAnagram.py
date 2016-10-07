class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        countMap = {}

        for ch in s:
            if ch.lower() in countMap:
                countMap[ch.lower()] += 1
            else:
                countMap[ch.lower()] = 1

        for ch in t:
            if ch.lower() in countMap:
                countMap[ch.lower()] -= 1
            else:
                countMap[ch.lower()] = -1

            if countMap[ch.lower()] < 0:
                return False


        return True

