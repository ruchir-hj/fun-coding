class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max, mask = 0,0

        for i in xrange(31, -1, -1):
            mask = mask | (1 << i)
            prefixSet = set()

            for num in nums:
                prefixSet.add(num & mask)

            tmp = max | (1 << i)

            for prefix in prefixSet:
                if (tmp ^ prefix) in prefixSet:
                    max = tmp
                    break

        return max