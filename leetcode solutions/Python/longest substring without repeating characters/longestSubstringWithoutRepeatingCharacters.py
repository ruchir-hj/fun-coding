class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start, maxLength = 0, 0
        usedChar = {}

        for end in range(0, len(s)):
            if s[end] in usedChar and start <= usedChar[s[end]]:
                start = usedChar[s[end]] + 1
            else:
                maxLength = max(maxLength, end - start + 1)

            usedChar[s[end]] = end

        return maxLength












