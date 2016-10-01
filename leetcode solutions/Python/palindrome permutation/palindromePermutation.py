class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False

        frequencies = set()

        for ch in s:
            if ch in frequencies:
                frequencies.remove(ch)
            else:
                frequencies.add(ch)

        if len(s) % 2 == 0:
            return len(frequencies) == 0
        else:
            return len(frequencies) == 1
